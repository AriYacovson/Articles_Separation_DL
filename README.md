
# Articles_Separation_DL
A DL (Deep Learning) project developed for the Asif Library. They've provided positive feedback, highlighting significant time savings due to the project.

### Purpose
The primary goal of this project is to automate manual processes. One such task involves taking an entire book composed of multiple articles (provided in a single PDF file) and returning each article as a separate PDF file.

### Methodology
To achieve this, we trained a CNN (Convolutional Neural Network) model. We gathered training data by scraping articles that were already uploaded to the website. This data was then labeled, distinguishing between first pages of articles and subsequent pages.

## Implementation Details
### Data Collection
We utilized web scraping tools to extract articles from the Asif Library website. This ensured that our model was trained on genuine and relevant data, matching the actual use-case.

## Data Preprocessing
After obtaining the raw data, it underwent preprocessing. This included tasks like:

Converting images within the PDFs to a standard format and resolution suitable for the CNN model.

Handling any anomalies or inconsistencies in the data, such as corrupted files or missing pages.

### Model Training
Our CNN model was trained with a diverse set of articles to ensure robustness.

The model was optimized for both accuracy and speed, ensuring articles were separated quickly and correctly.
