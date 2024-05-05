from src.model.model_trainer import ModelTrainer
from transformers import AutoModelForCausalLM
from src.utils.data_utils import prepare_tokenizer, load_dataset, split_dataset, tokenize_dataset, SplitEnum
from src.utils.env_loader import MODEL_NAME, KOTLIN_DATASET_PATH, MODEL_OUTPUT_PATH


def main():
    model_name = MODEL_NAME
    kotlin_dataset_path = KOTLIN_DATASET_PATH
    output_dir = MODEL_OUTPUT_PATH

    model = AutoModelForCausalLM.from_pretrained(model_name)

    kotlin_dataset = load_dataset(kotlin_dataset_path)
    kotlin_train_data = split_dataset(kotlin_dataset, SplitEnum.TRAIN)
    tokenizer = prepare_tokenizer(model_name)
    tokenized_kotlin_train_dataset = tokenize_dataset(tokenizer, kotlin_train_data)

    model_trainer = ModelTrainer(model, tokenizer, tokenized_kotlin_train_dataset, output_dir)
    model_trainer.setup_lora()
    model_trainer.train()
    model_trainer.save_model()


if __name__ == "__main__":
    main()
