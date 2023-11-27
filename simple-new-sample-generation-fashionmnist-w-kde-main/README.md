# Simple New Sample Generation FashionMNIST w/KDE
A primitive GAN, a sample data generator with Kernel Density Estimation

![255333410-173b82db-d577-4314-8ace-84eb96e2c570](https://github.com/john-fante/my-machine-learning-theory-implementation/assets/50263592/ee6fc876-dc30-40a7-8757-576db095fa02)


I tried to create <b>a basic sample data generator with Kernel Density Estimation</b>. Main goal of this project is creating new samples from original distribution of data. Kernel density is very handy for sampling from discrete distribution.

This project based on this example from sklearn docs -> https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html<br>
My similar project using Fashion MNIST is there -> [https://www.kaggle.com/banddaniel/simple-new-sample-generation-fashionmnist-w-kde](https://www.kaggle.com/banddaniel/simple-new-sample-generation-from-mnist-w-kde)
<br/>
<hr>
<h3>In this method, I follow these steps;</h3>
1. StandardScaler for scaling data.<br>
2. PCA for reducing dimension <span style="color:red">(..., 784) -> (..., 350)</span> I chose 350 component with trial and error.<br>
3. Applying KDE with gaussian kernel and 0.1 bandwith.<br>
4. Inversing all transform.<br>



## My results <br>

![255333477-15968294-db55-4fc9-aed7-44d8e4b0457f](https://github.com/john-fante/my-machine-learning-theory-implementation/assets/50263592/11940e68-c186-4cb5-b99d-000fc8607bd3)
