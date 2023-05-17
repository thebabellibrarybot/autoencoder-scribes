# autoencoder-scribes
autoencoder and dataloaders for running anomaly detection in medieval scribes version of the MNIST dataset 
##### view the runs on wandb: 
[Wandb report of auto-encoder training](https://wandb.ai/babelbots/Autoencoder-Scribes/reports/Overview-of-autoencoder-for-medieval-MNIST-dataset--Vmlldzo0MzgyOTU5)
### Dataset

  Scrapes [Late Medeival Scribes](https://www.medievalscribes.com/index.php?page=about&nav=off) for images of textura font alphabet and transform images into 28x28 binary images with corresponding labels. Data is compiled by medevalists and historians and was developed by The Centre for Medieval Studies at the University of York and the University of Oxford with technical development provided by The Digital Humanities Institute, University of Sheffield. The project was funded by the Arts and Humanities Research Council

locations: `dataloaders/puppetter.py`

run: `python puppetter.py`

##### Example characters:

A: <img src="https://www.dhi.ac.uk/san/medievalscribes/images/Sloane1685-43v-a2.jpg" alt="Example Image" width="28">
D: <img src = "https://www.dhi.ac.uk/san/medievalscribes/images/eMusaeo116-13r-d3.jpg" alt = "Example Image D" width = "28">
G: <img src = 'https://www.dhi.ac.uk/san/medievalscribes/images/eMusaeo116-13r-g.jpg' alt = 'Example Image G' width = '28'>
H: <img src = 'https://www.dhi.ac.uk/san/medievalscribes/images/eMusaeo116-13r-h.jpg' alt = 'Example Image H' width = '28'>
R: <img src = 'https://www.dhi.ac.uk/san/medievalscribes/images/Add10340-10v-r2.jpg' alt = 'Example Image R' width = '28'>
S: <img src = 'https://www.dhi.ac.uk/san/medievalscribes/images/Harley4826-94v-s3.jpg' alt = 'Example Image S' width = '28'>
W: <img src = 'https://www.dhi.ac.uk/san/medievalscribes/images/EL26-A-13-1r-w2.jpg' alt = 'Example Image W' width = '28'>
Y: <img src = 'https://www.dhi.ac.uk/san/medievalscribes/images/Additional25718-47-y.jpg' alt = 'Example Image Y' width = '28'>

##### About the dataset:

  This dataset offers an image of each scribal hand in each medieval or early modern manuscript of the English writings of five principal authors of the late fourteenth and early fifteenth centuries: William Langland, Geoffrey Chaucer, John Gower, John Trevisa and Thomas Hoccleve. In addition to these overall aspect images of the scribal hands, brief descriptions of the manuscripts and images of sample letter forms for eight letters, a, d, g, h, r, s, w and y, are also provided. These letters were chosen as having the most variable forms in late medieval English scripts and thus the best distinguishing graphs of a scribal hand. Images of some wildcard letter forms (including thorn and yogh) for other letters or marks of punctuation that are distinctive to each scribal hand are also included in the dataset.
  
  While this dataset is well organized and archived the image structure is highly irregular following often times diverting from a single character display case to a whole word or phrase display case, which will include the letter in question. Additionally there are instances of diviation from a normal occurance of each character in question such as instance where, in line with abreviation standards at the time, there may be a doubling of a character or a character with an additional synatic marking. The use-case for an autoencoder here is to find extrem oddities within this dataset to filter out, or create unique annotations for.
 

  
### Autoencoder

TBD:

#### basic usage

`git clone https://github.com/thebabellibrarybot/autoencoder-scribes`

#### TODO: Add req.txt

 `python -m venv sribes`

 `source scribes/bin/activate`
 
 `pip install -r req.txt`
 
 `python3 getdata.py`

##### Training

`python3 app.py`

parameters:

 `-- wandb: 'project-name', [default = 'autoencoder-scribes']`
 
 `-- train: true/false, [default = true]`
 
 `-- inference: true/false, [default = true, this will train then run and log inference results]`
 
 `-- epochs: int, [default = 10]`
 
 `-- batch_size: int, [ddefault = 32]`
 
 `-- lr: int, [default = .001 for ssim loss_fn]`
 
 `-- sweep: true/false, [default = false, will decide wether or not to run a wandb sweep with metrics set to minimize outliers]`
