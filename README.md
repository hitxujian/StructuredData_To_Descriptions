# Generating Descriptions from Structured Data Using a Bifocal Attention Mechanism and Gated Orthogonalization


Given Wikipedia infoboxes for personalities generate natural language text


## Requirements:
* [tensorflow-0.12](https://www.tensorflow.org/versions/r0.12/get_started/os_setup)
* [gensim](https://pypi.python.org/pypi/gensim)
* [nltk](http://www.nltk.org/install.html)
* [matplotlib](https://matplotlib.org/users/installing.html)

## Data Download:
    The English Biography Dataset has been released as a part of the following work: .
    The dataset is avaliable at link : [WikiBio] (https://github.com/DavidGrangier/wikipedia-biography-dataset)
    You can also use the following command to download the dataset and convert it to the format
    required by the models given:
    sh data_extraction_scripts/get_biography_dataset.sh

## Pretrained Embeddings
    Download the pretrained embeddings for a given language and then store it to the destination folder. 
    * English Embedding: bash data_extraction_scripts/extract_embeddings.sh english english_embedding
    * French  Embedding: bash data_extraction_scripts/extract_embedding.sh french french_embedding
    * German  Embedding: bash data_extraction_scripts/extract_embeddings.sh german german_embedding
    
    
## Various Proposed Model: Training
    cd code
    * To run only the Seq2seq model:
      ./train.sh seq2seq english
    * To run the hierarchy model:
       ./train.sh hierarchy english
    * To run the stay_on + never_look_back model:
        ./train.sh nlb english
    * To run the mei++ model:
        ./train.sh mei_plus english
   
    Note that the second argument could take "german" "french" "weathergov" also as an argument 
    
    To tweak the hyperparameters for the above models please do the required changes in train.sh.
    
    The best hyperparameter setting for "german" and "french" dataset has been mentioned in the 
    comments in train.sh
    
 ## Various Proposed Models: Inference
     Make sure that the current working directory is code/
    
     The syntax for running the inference is also similar to running the training 
 
     * Seq2seq model:
      ./test.sh seq2seq english
     *  Hierarchy model:
       ./test.sh hierarchy english
     * stay_on + never_look_back model:
        ./test.sh nlb english
     * mei++ model:
        ./test.sh mei_plus english
 
 
 ## Post Processing Scripts: Copy Mechanism and Generate Attention Weight Plots:
     cd postprocess_scripts
     
     # sh extract_labels_plots.sh <output_dir> <data_directory>
     sh extract_labels_plots.sh ../output ../data_french
     
     Please note:
        * The post process copy will not work for Mei_plus model, as the attention mechanism in this model, 
        never focusses on the token level encoder. Also it is not necessary for weathergov data, as the vocabulary
        size is very small, thus you could get the probability distribution across all the tokens
        * The Attention Weight Plots have been against field level information. Thus this part of the
        code won't work for basic seq2seq model.
 
 
 
 ## Some sample predictions and plots generated:
 ### English WikiBio
 * **NLB Predicted Summary**      :  john ford -lrb- born july 31 , 1966 in belle glade , florida -rrb- is a former american football wide receiver in the national football league for the detroit lions . 
 * **Hierarchy Predicted Summary**: john ford -lrb- born july 31 , 1966 in belle glade , florida -rrb- is a former american football wide receiver in the national football league .
 * **Seq2seq Predicted Summary**  :  john ford -lrb- born april 31 , 1966 in belle glade , florida -rrb- is a former american football wide receiver in the national football league for the . 

 * **Ground Truth** : John Allen Ford -lrb born July 31, 1966 -rrb-  is a former American football wide receiver in the National Football League for the Detroit Lions.
 
     <center>
     <table style="width:100%">
     <tr>
     <th> Hierarchy </th>
     <th> Never Look Back </th>
     </tr>
     <tr>
     <td><img src="/images/eng_hier.jpg" height="400" width="400"> </td>
     <td> <img src="/images/eng_nlb.jpg" height="400" width="400"></td>
     </tr>
     </table>
     </center>


 ### German WikiBio
 * **NLB Predicted Summary**      :  matthias hagner -lrb- 15 .august 1968 in köln -rrb- ist ein ehemaliger deutscher fußballspieler und jetziger - trainer .
 * **Hierarchy Predicted Summary**:  matthias hagner -lrb- * 15 .oktober 1968 in köln -rrb- ist ein ehemaliger deutscher fußballspieler und - trainer .
 * **Seq2seq Predicted Summary**  :  matthias kurzname -lrb- * 15 .august 1968 in kurzname -rrb- ist ein deutscher fußballspieler . 

 * **Ground Truth** : Matthias Hagner (15. August 1974 in Gießen) ist ein ehemaliger deutscher Fußballspieler und jetziger -trainer.
 
     <center>
     <table style="width:100%">
     <tr>
     <th> Hierarchy </th>
     <th> Never Look Back </th>
     </tr>
     <tr>
     <td><img src="/images/german_hier.jpg" height="400" width="400"> </td>
     <td> <img src="/images/german_nlb.jpg" height="400" width="400"></td>
     </tr>
     </table>
     </center>

## Evaluation Scripts:
Sources Referred for Evaluation script are same as that mentioned in Lebret et al, 2016:
* [Bleu_4](https://github.com/tylin/coco-caption) 
* [ROUGE_4](https://github.com/gregdurrett/berkeley-doc-summarizer/blob/master/rouge/ROUGE/ROUGE-1.5.5.pl)
* [NIST_4](ftp://jaguar.ncsl.nist.gov/mt/resources/mteval-v13.pl)

