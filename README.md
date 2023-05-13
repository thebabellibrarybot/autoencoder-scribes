# autoencoder-scribes
autoencoder and dataloaders for running anomaly detection in medieval scribes version of the MNIST dataset 

### Dataset

  Scrapes [Late Medeival Scribes](https://www.medievalscribes.com/index.php?page=about&nav=off) for images of textura font alphabet and transform images into 28x28 binary images with corresponding labels. Data is compiled by medevalists and historians and was developed by The Centre for Medieval Studies at the University of York and the University of Oxford with technical development provided by The Digital Humanities Institute, University of Sheffield. The project was funded by the Arts and Humanities Research Council

locations: `dataloaders/puppetter.py`

run: `python puppetter.py`

##### About the dataset:

  This dataset offers an image of each scribal hand in each medieval or early modern manuscript of the English writings of five principal authors of the late fourteenth and early fifteenth centuries: William Langland, Geoffrey Chaucer, John Gower, John Trevisa and Thomas Hoccleve. In addition to these overall aspect images of the scribal hands, brief descriptions of the manuscripts and images of sample letter forms for eight letters, a, d, g, h, r, s, w and y, are also provided. These letters were chosen as having the most variable forms in late medieval English scripts and thus the best distinguishing graphs of a scribal hand. Images of some wildcard letter forms (including thorn and yogh) for other letters or marks of punctuation that are distinctive to each scribal hand are also included in the dataset.
  
  While this dataset is well organized and archived the image structure is highly irregular following often times diverting from a single character display case to a whole word or phrase display case, which will include the letter in question. Additionally there are instances of diviation from a normal occurance of each character in question such as instance where, in line with abreviation standards at the time, there may be a doubling of a character or a character with an additional synatic marking. The use-case for an autoencoder here is to find extrem oddities within this dataset to filter out, or create unique annotations for.
  
##### Example characters:

A: <img src="https://www.dhi.ac.uk/san/medievalscribes/images/Sloane1685-43v-a2.jpg" alt="Example Image" width="28">

  
### Autoencoder

  TBD
