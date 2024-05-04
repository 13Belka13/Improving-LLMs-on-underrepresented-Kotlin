from peft import LoraConfig, get_peft_model
from transformers import TrainingArguments, Trainer, DataCollatorForLanguageModeling


class ModelTrainer:
    def __init__(self, model, tokenizer, train_dataset, output_dir):
        self.model = model
        self.tokenizer = tokenizer
        self.train_dataset = train_dataset
        self.output_dir = output_dir

    def setup_lora(self):
        config = LoraConfig(
            r=16,
            lora_alpha=16,
            target_modules=["dense", "fc2", "q_proj", "k_proj", "v_proj"],
            lora_dropout=0.05,
            bias="none",
            task_type="CAUSAL_LM"
        )
        self.model = get_peft_model(self.model, config)

    def train(self):
        training_args = TrainingArguments(
            output_dir=self.output_dir,
            per_device_train_batch_size=4,
            gradient_accumulation_steps=1,
            learning_rate=2e-4,
            num_train_epochs=1,
            save_strategy="epoch"
        )
        data_collator = DataCollatorForLanguageModeling(tokenizer=self.tokenizer, mlm=False)
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=self.train_dataset,
            data_collator=data_collator
        )
        trainer.train()

    def save_model(self):
        self.model.save_pretrained(self.output_dir)