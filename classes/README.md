# Classes

This work is devoted to practive in making Python classes

Classes directory consists of code directory with ipython notebook and regular
.py file with same content (but python notebook also have code that demonstrates 
working of classes presented in work)

Classes presented:

1) RomaToday

Objects of this class modeles Roma at a current day.

Attributes:

* mood : good, bad or angry
* lecturer : is he a lecturer today or not
* location : in DAS or elsewhere

Methods:
* play_xbox : will play xbox only when Roma is in the DAS
* help_students : depends on mood. When Roma has good mood, he will help students
directly. In bad mood he will sent to youtuve python playlist. In angry mood he 
will sent you to google
* drink_beer : he will not drink beer if he is a lecturer today


2) RNA

Objects of this class modeles sequence

Attributes:

* sequence : a sequence of RNA 

Methods:

* translation : translates the RNA sequence into protein sequence
* reverse_transcription: transcribes RNA into DNA

3) PlusSet

Objects of this class modeles Python sets without minus digits

Attributes:

* elemetns : elements of the set

Methods:

* add: adds one element to set. Will not add element if its value is below zero
* update: can add several elements. Elements below zero will not be added

4) FastaStat

Objects of this class modeles fastq file and allows operations with this file

Attributes:

* path : path to fastq file

Methods:

* modified __str__: when object is printed it returns path to fastq file
* count_seq: counts the number of reads
* len_hist: plots the histogram of reads length distribution
* gc_content: calculates the overall part of G and C bases in all reads in %
* four_meer_hist : plots the histogram of frequencies of all 4-meers presented
in fastq file
* stats : uses count_seq, len_hist, gc_content and four_meer_hist one after another




