# - Test -
My approach to the task at hand was to keep discrete sets of functionality in discrete modules, enabling each stage,
 extraction, transformation and consumption, to be as agnostic to the other stages as possible.
 
 Keeping responsibilities so separated gives one the freedom to alter the method of extraction 
 (say from reading a local file to reading from s3 or to making a REST call),
 without the transformation operators knowing or caring about HOW they got the data.
 Similarly, separating out the pieces responsible for final output means one 
 can add or remove consumers without affecting the extractors or transformers 