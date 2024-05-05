import argparse

from transformers import AutoModelForCausalLM

from src.utils.evaluation import evaluation
from src.utils.data_utils import load_model
from src.utils.env_loader import KOTLIN_DATASET_PATH, MODEL_NAME, PYTHON_DATASET_PATH, MODEL_PATH


def main(use_default=False):
    model_name = MODEL_NAME
    kotlin_dataset_path = KOTLIN_DATASET_PATH
    python_dataset_path = PYTHON_DATASET_PATH
    model_path = MODEL_PATH

    if use_default:
        model = AutoModelForCausalLM.from_pretrained(model_name)
    else:
        model = load_model(model_name, model_path)

    evaluation(model, model_name, kotlin_dataset_path, python_dataset_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Evaluate a model on Kotlin and Python datasets.')
    parser.add_argument('--use_default', action='store_true',
                        help='Use pretrained model instead of loading from checkpoint')

    args = parser.parse_args()

    main(args.use_default)
