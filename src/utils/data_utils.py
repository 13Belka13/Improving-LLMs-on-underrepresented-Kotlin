from enum import Enum

from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM

from src.data.dataset_loader import DatasetLoader
from src.data.dataset_splitter import DatasetSplitter
from src.evaluator.accuracy_evaluator import AccuracyEvaluator
from src.evaluator.perplexity_evaluator import PerplexityEvaluator
from src.preprocessing.dataset_tokenizer import DatasetTokenizer
from src.utils.logger import Logger

logger = Logger().get_logger()


class SplitEnum(Enum):
    TRAIN = "train_test"
    TEST = "train_valid_test"


def load_dataset(dataset_path):
    logger.info(f"Loading dataset from {dataset_path}")
    dataset_loader = DatasetLoader(dataset_path)
    dataset = dataset_loader.load_dataset()
    logger.info(f"Dataset loaded successfully")
    return dataset


def split_dataset(dataset, split: SplitEnum = SplitEnum.TRAIN):
    logger.info("Splitting dataset into train and test data")
    dataset_splitter = DatasetSplitter(dataset)
    train_data, test_data = dataset_splitter.split_dataset()
    logger.info("Dataset split completed")
    return test_data if split == SplitEnum.TEST else train_data


def prepare_tokenizer(model_name, padding_side='right'):
    logger.info(f"Preparing tokenizer for model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side=padding_side)
    tokenizer.pad_token = tokenizer.eos_token
    logger.info("Tokenizer prepared successfully")
    return tokenizer


def tokenize_dataset(tokenizer, data):
    logger.info("Tokenizing test dataset")
    dataset_tokenizer = DatasetTokenizer(tokenizer)
    tokenized_dataset = dataset_tokenizer.prepare_dataset(data)
    logger.info("Dataset tokenized successfully")
    return tokenized_dataset


def load_model(model_name, model_path):
    logger.info(f"Loading model: {model_name}")
    model = AutoModelForCausalLM.from_pretrained(model_name)
    logger.info(f"Loading fine-tuned model from {model_path}")
    model = PeftModel.from_pretrained(model, model_path)
    logger.info("Model loaded successfully")
    return model


def evaluate_perplexity(model, tokenizer, tokenized_test_dataset):
    logger.info("Evaluating perplexity")
    perplexity_evaluator = PerplexityEvaluator(model, tokenizer, tokenized_test_dataset)
    perplexity = perplexity_evaluator.evaluate_perplexity()
    logger.info(f"Perplexity evaluation completed. Perplexity: {perplexity:.2f}")
    return perplexity


def evaluate_accuracy(model, tokenizer, tokenized_test_dataset):
    logger.info("Evaluating accuracy")
    accuracy_evaluator = AccuracyEvaluator(model, tokenizer, tokenized_test_dataset)
    accuracy = accuracy_evaluator.evaluate_accuracy()
    logger.info(f"Accuracy evaluation completed. Accuracy: {accuracy:.4f}")
    return accuracy

