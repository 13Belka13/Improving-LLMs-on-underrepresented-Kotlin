from src.utils.logger import Logger
from src.utils.data_utils import prepare_tokenizer, split_dataset, SplitEnum, \
    tokenize_dataset, evaluate_perplexity, load_dataset, evaluate_accuracy

import logging
from src.utils.data_utils import prepare_tokenizer, split_dataset, SplitEnum, \
    tokenize_dataset, evaluate_perplexity, load_dataset, evaluate_accuracy


def evaluate_model(model, model_name, dataset_path, language):
    logger = logging.getLogger(__name__)

    tokenizer = prepare_tokenizer(model_name)

    logger.info(f"Starting evaluation on {language} dataset")
    dataset = load_dataset(dataset_path)
    test_data = split_dataset(dataset, SplitEnum.TEST)
    tokenized_test_dataset = tokenize_dataset(tokenizer, test_data)

    perplexity = evaluate_perplexity(model, tokenizer, tokenized_test_dataset)

    tokenizer_left_padding = prepare_tokenizer(model_name, padding_side='left')
    accuracy = evaluate_accuracy(model, tokenizer_left_padding, tokenized_test_dataset)

    logger.info(f"{language} Accuracy: {accuracy:.4f}")
    logger.info(f"{language} Perplexity: {perplexity:.2f}")

    return accuracy, perplexity


def evaluation(model, model_name, kotlin_dataset_path, python_dataset_path):
    logging.info("Starting evaluation")

    kotlin_accuracy, kotlin_perplexity = evaluate_model(
        model, model_name, kotlin_dataset_path, "Kotlin"
    )
    python_accuracy, python_perplexity = evaluate_model(
        model, model_name, python_dataset_path, "Python"
    )

    logging.info("Evaluation complete. Results:")
    logging.info(f"Kotlin Accuracy: {kotlin_accuracy:.4f}")
    logging.info(f"Kotlin Perplexity: {kotlin_perplexity:.2f}")
    logging.info(f"Python Accuracy: {python_accuracy:.4f}")
    logging.info(f"Python Perplexity: {python_perplexity:.2f}")
