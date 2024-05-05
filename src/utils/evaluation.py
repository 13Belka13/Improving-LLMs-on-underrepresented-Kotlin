from src.utils.logger import Logger
from src.utils.data_utils import prepare_tokenizer, split_dataset, SplitEnum, \
    tokenize_dataset, evaluate_perplexity, load_dataset, evaluate_accuracy


def evaluation(model, model_name, kotlin_dataset_path, python_dataset_path):
    logger = Logger().get_logger()

    tokenizer = prepare_tokenizer(model_name)

    logger.info("Starting evaluation on Kotlin dataset")
    kotlin_dataset = load_dataset(kotlin_dataset_path)
    kotlin_test_data = split_dataset(kotlin_dataset, SplitEnum.TEST)
    tokenized_kotlin_test_dataset = tokenize_dataset(tokenizer, kotlin_test_data)
    kotlin_perplexity = evaluate_perplexity(model, tokenizer, tokenized_kotlin_test_dataset)
    kotlin_accuracy = evaluate_accuracy(model, tokenizer, tokenized_kotlin_test_dataset)

    logger.info("Starting evaluation on Python dataset")
    python_dataset = load_dataset(python_dataset_path)
    python_test_data = split_dataset(python_dataset, SplitEnum.TEST)
    tokenized_python_test_dataset = tokenize_dataset(tokenizer, python_test_data)
    python_perplexity = evaluate_perplexity(model, tokenizer, tokenized_python_test_dataset)
    python_accuracy = evaluate_accuracy(model, tokenizer, tokenized_python_test_dataset)

    logger.info("Evaluation complete. Results:")
    logger.info(f"Kotlin Accuracy: {kotlin_accuracy:.4f}")
    logger.info(f"Kotlin Perplexity: {kotlin_perplexity:.2f}")
    logger.info(f"Python Accuracy: {python_accuracy:.4f}")
    logger.info(f"Python Perplexity: {python_perplexity:.2f}")
