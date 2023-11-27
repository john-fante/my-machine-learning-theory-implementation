## Hassanat Distance Implementation w/KNN

<p>I tried to implement one of the relatively new distance metrics, Hassanat, in two datasets and compare it with the Minkowski distance result.
</p><br>

<img width="1111" alt="258535917-496e9a54-5121-4360-bef1-12416e130811" src="https://github.com/john-fante/my-machine-learning-theory-implementation/assets/50263592/9fd2a0a4-c5dc-4d70-b563-9d704397c8eb">

<i > Hassanat distance metric formula [1] </i><br>

## Result
<p>
All experiments took place with cross-validation. There is improvement in two trials with respect to the cross-validation score over the entire dataset.In the last trial, there was a decrease in performance.</p><br>

<span style="color:#e74c3c;"> Trial 1 </span> Breast Cancer Wisconsin Dataset <br>
<span style="color:#e74c3c;"> Trial 2 </span> Wine Quality Dataset <br>
<span style="color:#e74c3c;"> Trial 3 </span> Iris Dataset
<br>
<br>

|         	| Minkowski 	| Hassanat 	| Improvement 	|
|---------	|-----------	|----------	|-------------	|
| Trial 1 	| 90.857 %  	| 94.908 % 	| +4.051 %    	|
| Trial 2 	| 44.620 %  	| 50.480 % 	| +5.86 %     	|
| Trial 3 	| 96.667 %  	| 95.333 % 	| -1.334 %    	|




## Reference 
[1] https://doi.org/10.1109/ETCEA57049.2022.10009844
