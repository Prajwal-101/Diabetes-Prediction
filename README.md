# Diabetes-Prediction
Comparative analysis of Diabetes Prediction using different Machine Learning Algorithms.

---------------------------------------------------------------------------------------------------------

**AIM OF THE PROJECT**

The aim of this project is to develop a system which can perform early prediction of diabetes for 
a patient with a higher accuracy by combining the results of different machine learning techniques.

---------------------------------------------------------------------------------------------------------

**WHAT IS DIABETES**

Diabetes is a chronic disease with the potential to cause a worldwide health care crisis. According to International 
Diabetes Federation 537 million people were living with diabetes across the whole world in 2021. By 2030, this will be
doubled as 643 million. Diabetes is a disease caused due to the increase level of blood glucose. This high blood glucose 
produces the symptoms of frequent urination, increased thirst, and increased hunger. Diabetes is a one of the leading cause 
of blindness, kidney failure, amputations, heart failure and stroke. When we eat, our body turns food into sugars, or glucose. 
At that point, our pancreas is supposed to release insulin. Insulin serves as a key to open our cells, to allow the glucose to 
enter and allow us to use the glucose for energy. But with diabetes, this system does not work. Type 1 and type 2 diabetes are
the most common forms of the disease, but there are also other kinds, such as gestational diabetes, which occurs during 
pregnancy, as well as other forms. 

Machine learning is an emerging scientific field in data science dealing with the ways in which machines learn from experience. 

---------------------------------------------------------------------------------------------------------

**ALGORITHMS USED**

**Support Vector Machine:**

A support vector machine builds a hyper-plane or set of hyperplanes in a high or limitless dimensional space, 
which can be utilized for classification, regression or different undertakings. Instinctively, a great separation 
is accomplished by the hyperplane that has the biggest separation to the closest training point of any class 
(supposed as functional margin), since all in all the bigger the margin the lower the generalisation error of
the classifier.

The SVM has typically three kernels: 
i) Linear Kernel
ii) Polynomial Kernel
iii) Radial Basis Function or Gaussian Kernel
Linear Kernels work perfectly on linearly separable data, however when data is linearly inseparable, RBF kernel is
used which projects the data into an n-dimensional higher space and computes all the calculations there.

_Algorithm-_

• Select the hyper plane which divides the class better.<br>
• To find the better hyper plane you have to calculate the distance between the planes and the data which is called Margin.<br>
• If the distance between the classes is low then the chance of miss conception is high and vice versa. So we need to<br>
• Select the class which has the high margin. <br>

        		Margin = distance to positive point + Distance to negative point.

**Decision Tree:**

A decision tree (DT) is a supervised learning technique that is mostly used for classification tasks and is also helpful in 
discovering relevant features and patterns in large databases, thus serving as a powerful means of discrimination and 
predictive modeling [19]. Each node in a Decision tree, or Decision node and Leaf node, consists of a test for an attribute, 
which creates one of the two branches in the tree that descends from that node.

_Algorithm-_

• Construct tree with nodes as input feature.<br>
• Select feature to predict the output from input feature whose information gain is highest.<br>
• The highest information gain is calculated for each attribute in each node of tree.<br>
• Repeat step 2 to form a subtree using the feature which is not used in above node.<br>


**Random Forest Classifier:**

It is an ensemble learning method that uses multiple decision trees, It is type of ensemble learning method and also used for 
classification and regression tasks. The accuracy it gives is grater then compared to other models. This method can easily 
handle large datasets. Random Forest is developed by Leo Bremen. It is popular ensemble Learning Method. Random Forest Improve 
Performance of Decision Tree by reducing variance. It operates by constructing a multitude of decision trees at training time 
and outputs the class that is the mode of the classes or classification or mean prediction (regression) of the individual trees.

_Algorithm-_

• The first step is to select the “R” features from the total features “m” where R<<M.<br>
• Among the “R” features, the node using the best split point.<br>
• Split the node into sub nodes using the best split.<br>
• Repeat a to c steps until ”l” number of nodes has been reached.<br>
• Built forest by repeating steps a to d for “a” number of times to create “n” number of trees.<br>


