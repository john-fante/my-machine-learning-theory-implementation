# Simple New Sample Generation from MNIST w/KDE

![254902949-b0d5a7f9-91af-46b9-93e1-c7059ed5aab5](https://github.com/john-fante/my-machine-learning-theory-implementation/assets/50263592/3e4f9312-e5b0-4a12-bd4a-c82792781723)


I tried to create <b>a basic sample data generator with Kernel Density Estimation</b>. Main goal of this project is creating new samples from original distribution of data. Kernel density is very handy for sampling from discrete distribution.

This project based on this example from sklearn docs -> https://scikit-learn.org/stable/auto_examples/neighbors/plot_digits_kde_sampling.html<br>
My similar project using Fashion MNIST is there -> https://www.kaggle.com/banddaniel/simple-new-sample-generation-fashionmnist-w-kde
<br/>
<hr>
<h3>In this method, I follow these steps;</h3>
1. StandardScaler for scaling data.<br>
2. PCA for reducing dimension <span style="color:red">(..., 784) -> (..., 350)</span> I chose 350 component with trial and error.<br>
3. Applying KDE with gaussian kernel and 0.1 bandwith.<br>
4. Inversing all transform.<br>

## My results <br>

![254906867-f3c32c07-d1b8-4249-817c-a048557417cb](https://github.com/john-fante/my-machine-learning-theory-implementation/assets/50263592/b0be1a43-1239-45ef-9a2a-5472c0121f1a)
