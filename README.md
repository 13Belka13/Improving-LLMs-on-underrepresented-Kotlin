# Kotlin Code Completion with Fine-Tuned Transformer Model

This project focuses on improving code completion for underrepresented programming languages, specifically Kotlin, using a fine-tuned Transformer model. The goal is to adapt a Python-oriented pre-trained Transformer model, such as Phi-1.5, to perform code completion on Kotlin code and evaluate its performance on both Kotlin and Python datasets.

## Dataset

The Kotlin/Python code completion dataset is created by extracting code from a large open source Kotlin/Pyton project. The extracted code is used to train and evaluate the code completion model.

## Model

A pre-trained Phi-1.5 transformer model, originally oriented towards Python, is refined on the Kotlin dataset to adapt it for code completion in Kotlin. The performance of the model is then evaluated on both the test part of the Kotlin and Python dataset.

## Repository Structure

The repository is organized as follows:

- `notebooks/`: Contains Jupyter notebooks for experimentation and analysis.
- `src/`: Contains the source code for the project.
  - `code_preprocessor/`: Code preprocessing utilities.
  - `constants/`: Constant values used throughout the project.
  - `data/`: Data-related utilities and processing scripts.
  - `evaluator/`: Evaluation scripts and metrics.
  - `file_retriever/`: File retrieval utilities for dataset creation.
  - `function_extractor/`: Function extraction utilities for dataset creation.
  - `model/`: Model-related utilities and training scripts.
  - `preprocessing/`: Data preprocessing utilities.
  - `repository_client/`: Client for interacting with code repositories.
  - `utils/`: Miscellaneous utility functions.
  - `main.py`: Main entry point for running the project.
- `tests/`: Contains unit tests for the project.
- `.env.example`: Example environment configuration file.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file, providing an overview of the project and instructions to run it.
- `requirements.txt`: Lists the required Python dependencies for the project.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/13Belka13/Improving-LLMs-on-underrepresented-Kotlin.git
   cd Improving-LLMs-on-underrepresented-Kotlin
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file based on the provided `.env.example` file and configure the necessary environment variables:
   ```
   GITHUB_TOKEN=your_github_token
   MODEL_NAME="microsoft/phi-1_5"
   KOTLIN_DATASET_PATH=your_kotlin_dataset_path
   PYTHON_DATASET_PATH=your_python_dataset_path
   MODEL_PATH=your_model_path
   MODEL_OUTPUT_PATH="phi-1-5-finetuned-kotlin"
   PYTHON_REPO_USERNAME="python"
   PYTHON_REPO_NAME="cpython"
   PYTHON_MAX_FILES=10000
   PYTHON_OUTPUT_FILE="data/python_dataset.txt"
   KOTLIN_REPO_USERNAME="JetBrains"
   KOTLIN_REPO_NAME="kotlin"
   KOTLIN_MAX_FILES=10000
   KOTLIN_OUTPUT_FILE="data/kotlin_dataset.txt"
   ```

   Here's a brief description of each environment variable:
   - `GITHUB_TOKEN`: Your GitHub personal access token for accessing repositories.
   - `MODEL_NAME`: The name of the pre-trained Transformer model to be used (e.g., "microsoft/phi-1_5").
   - `KOTLIN_DATASET_PATH`: The path to the Kotlin dataset file.
   - `PYTHON_DATASET_PATH`: The path to the Python dataset file.
   - `MODEL_PATH`: The path to the fine-tuned model directory.
   - `MODEL_OUTPUT_PATH`: The output path for saving the fine-tuned model.
   - `PYTHON_REPO_USERNAME`: The username of the Python repository owner.
   - `PYTHON_REPO_NAME`: The name of the Python repository.
   - `PYTHON_MAX_FILES`: The maximum number of Python files to retrieve from the repository.
   - `PYTHON_OUTPUT_FILE`: The output file path for storing the Python dataset.
   - `KOTLIN_REPO_USERNAME`: The username of the Kotlin repository owner.
   - `KOTLIN_REPO_NAME`: The name of the Kotlin repository.
   - `KOTLIN_MAX_FILES`: The maximum number of Kotlin files to retrieve from the repository.
   - `KOTLIN_OUTPUT_FILE`: The output file path for storing the Kotlin dataset.

   Make sure to replace the placeholders with your actual values.

## Usage

To run the code parser and generate the datasets, execute the following command:
```
python src/collect_data.py
```

To fine-tune the model, run:
```
python src/fine_tune_model.py
```

To evaluate the model, use:
```
python src/evaluate_model.py
```

You can add the `--use_default` flag to evaluate the non-fine-tuned model.

## Metrics

The project uses the following metrics to evaluate the performance of the code completion model:

1. **Perplexity**: Perplexity is a commonly used metric in language modeling that measures how well the model predicts the next token in a sequence. A lower perplexity indicates better performance, as it suggests that the model is more confident in its predictions. Perplexity is calculated as the exponential of the average negative log-likelihood of the target tokens.

2. **Accuracy**: Accuracy is a straightforward metric that measures the percentage of correctly predicted tokens. It provides an intuitive understanding of how often the model makes the right predictions. Accuracy is calculated as the number of correctly predicted tokens divided by the total number of tokens.

The choice of these metrics is based on their relevance to the code completion task and their widespread use in the evaluation of language models:

- Perplexity is a standard metric in language modeling and provides a measure of the model's overall predictive power. It is particularly useful for comparing different models or configurations.
- Accuracy is an easily interpretable metric that directly measures the correctness of the model's predictions. It gives a clear indication of how often the model suggests the right code completions.

### Results

The following table presents the evaluation results for the default (non-fine-tuned) model and the fine-tuned model on the Kotlin dataset:

| Model          | Dataset | Accuracy | Perplexity |
|----------------|---------|----------|------------|
| Default        | Kotlin  | 0.0031   | 94.78      |
|                | Python  | 0.0067   | 6.67       |
| Fine-tuned     | Kotlin  | 0.0096   | 62.82      |
|                | Python  | 0.0180   | 5.71       |

As shown in the table, the fine-tuned model achieves better performance compared to the default model on both the Kotlin and Python datasets. The fine-tuned model has higher accuracy and lower perplexity, indicating that it is more effective at predicting the next token in the code sequences.

The results demonstrate the impact of fine-tuning on improving the model's performance for code completion. By adapting the pre-trained model to the specific programming language (Kotlin), the fine-tuned model is able to capture the language-specific patterns and provide more accurate code completions.

It's important to note that while the fine-tuned model shows improvement, there is still room for further enhancement. The accuracy values are relatively low, suggesting that the model has limitations in correctly predicting the next token in many cases. However, the focus of this project was on establishing a functional pipeline for code completion in Kotlin, and the fine-tuned model serves as a starting point for future improvements.

## Strengths

1. **Extensibility**:
- The project uses OOP principles and is divided into modules, making it easy to add support for new programming languages or include additional pre-trained models.
- Additionally, this approach allows for easy modification of data collection piplene, model training, or adding additional metrics for model evaluation.
- The use of environment variables for customization allows flexibility to adapt the project to different environments or datasets without making changes to the code.

2. **Integrability**:
- The project's pipeline is designed in a way that allows for easy integration into larger solutions or codebases.
- The modular structure of the project, with separate components for data preprocessing, model training, and evaluation, enables seamless incorporation into existing workflows or pipelines.
- The project's code and functionality can be easily wrapped or exposed as an API, making it straightforward to incorporate the code completion capabilities into other applications or services.

By designing the project with integrability in mind, it becomes possible to leverage the code completion capabilities developed in this solution as a component of a larger, more comprehensive system. This could involve integrating the code completion functionality into an IDE plugin, a web-based code editor, or a code analysis and recommendation tool.
The integrability aspect of the project highlights its potential to be a valuable building block in the development of more sophisticated and feature-rich code assistance tools. By providing a solid foundation for code completion in Kotlin, this project can contribute to the creation of more comprehensive solutions that combine multiple code analysis and generation techniques.
Overall, the integrability of the project is a significant strength that enables its seamless incorporation into larger codebases and facilitates its usage as a component in more extensive code development and analysis workflows.

3. **Code tokenization**
- The project employs a tokenization approach that preserves only the basic language functions and reserved words while replacing other tokens with placeholders. This technique enhances the extensibility of the solution by focusing on the core language constructs and reducing the complexity of the code representation.

## Weaknesses

1. **Lack of Metrics**:
- The project could benefit from a more comprehensive set of evaluation metrics to assess the performance of the code completion model.

2. **Lack of Patterns in Some Places**:
- The project could benefit from the use of established design patterns or architectures in certain areas to improve code organization and maintainability.

3. **Weak Model Quality**:
- Although the model shows an improvement in metrics compared to the non-fine-tuned model, the overall quality of the code completion predictions may still be suboptimal.
The project could benefit from further experimentation with different model architectures, hyperparameter tuning, or data augmentation techniques to improve the model's performance.
However, it's important to note that the challenge description did not explicitly emphasize achieving the highest model quality, and the focus was placed on other aspects of the project.
Despite these weaknesses, the project demonstrates a functional pipeline for fine-tuning a pre-trained Transformer model for code completion in Kotlin. The extensibility and integrability of the solution are notable strengths that contribute to its potential usefulness and adaptability.


Despite these weaknesses, the project demonstrates a functional pipeline for fine-tuning a pre-trained Transformer model for code completion in Kotlin. The extensibility and integrability of the solution are notable strengths that contribute to its potential usefulness and adaptability.
It's important to acknowledge that the project has room for improvement in terms of metrics, design patterns, and model quality. However, given the scope and objectives of the challenge, the solution successfully addresses the main goals of adapting a Python-oriented model to Kotlin code completion and providing a working pipeline for dataset creation, model fine-tuning, and evaluation.

## Colab Notebook

The Colab notebook used for training and evaluating the model can be found at: [Kotlin Code Completion with Fine-Tuned Transformer Model](https://drive.google.com/file/d/1EF-eCJUGmpSWh9mE089o5taBQp2I9t6p/view?usp=sharing).

## Hugging Face

The fine-tuned model is available on Hugging Face: [phi-1-5-finetuned-kotlin](https://huggingface.co/13Belka13/phi-1-5-finetuned-kotlin).

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or inquiries, please contact the project maintainer at [belik820@gmail.com](mailto:belik820@gmail.com).
