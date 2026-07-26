---
title: Implementing CNN with MPS
source: 杨萧玉
source_key: yulingtianxia
source_url: 'http://yulingtianxia.com/blog/2017/05/30/Implementing-CNN-with-MPS/'
original_language: zh
published: 2019-05-26
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c0282db2bd2a5ed8'
translated: n/a
---

> 原文：[Implementing CNN with MPS](http://yulingtianxia.com/blog/2017/05/30/Implementing-CNN-with-MPS/)　·　杨萧玉

# [Implementing CNN with MPS](http://yulingtianxia.com/blog/2017/05/30/Implementing-CNN-with-MPS/)

By [杨萧玉](https://plus.google.com/106642427004837273341?rel=author)

发表于 2017-05-30

1. 1. 理论基础

    1. 1.1. 卷积神经网络简介
    2. 1.2. 图片分类常用的数据和预设网络模型
    3. 1.3. 迁移学习
2. 2. 框架选择
3. 3. 数据采集
4. 4. Inception V3 pre-trained network

    1. 4.1. bottleneck features
    2. 4.2. Fine-tuning
5. 5. Convert HDF5 to binary .dat files
6. 6. Metal Performance Shaders

    1. 6.1. MPS 简介
    2. 6.2. 使用 MPS 构建网络并预测
7. 7. 总结
8. 8. Reference

最近一个月从零开始自学了下有关 iOS 上的机器学习相关知识，亲身实践了从数据采集到训练模型再到移动端预测的流程。理论知识学习路径为：**机器学习-\>深度学习-\>迁移学习**；实践框架学习路径为：**TensorFlow-\>Keras-\>MPS(iOS 10)**。最终完成一个简单的手势图像五分类问题，并预测 iOS 摄像头采集的图片。最终结果，训练集准确率 96.26%，交叉验证集准确率 73.86%。

## [#理论基础](#理论基础)理论基础

虽然结果导向很重要，但是我还是想从基础学起，而不是去急于去网上找现成的解决方案来调参。毕竟我的目的是拓宽知识面，开新的技能树。

第一周从零开始学习了 Coursera 上 Stanford Ng 教授的 [Machine Learning](https://www.coursera.org/learn/machine-learning/home) 经典课程，用 Matlab 编写了一些 Demo，用一周时间完成了原本需要 11 周时间的所有课程和考试，对机器学习的基础知识有了掌握。

![](http://wx3.sinaimg.cn/mw1024/642c5793ly1ff5ornniluj21kw0u3tn2.jpg)

机器学习大体可以分为有监督学习和无监督学习。带标签数据的有监督学习包含从最简单的线性回归到逻辑回归，再到神经网络和 SVM（支持向量机）。无监督学习包含大学竖直的 K-means 聚类，PCA(Principal Components Analysis) 降维。以及带标签数据的异常检测算法。为了确保机器学习的效果，需要通过看懂学习曲线决定下一步的工作，是解决 overfit 还是 underfit。使用交叉验证集和测试集评估模型时，如何平衡准确率和召回率，比如 F1 Score 指标。在数据预处理上要了解一些数据归一化标准化的方法。

光掌握机器学习的基础知识显然不够，大而全不如专而精。深度学习在图像识别领域大放异彩，其实深度学习是机器学习的一个分支，而深度学习领域最近在图像识别上应用最火的可能就是 CNN 了。所以在狂学深度学习的时候重点研究了下 CNN。

### [#卷积神经网络简介](#卷积神经网络简介)卷积神经网络简介

全连接网络权重过多，而卷积神经网络可以实现权值共享，引入了深度，数据为 3D 的。推荐查看 Stanford 的 [Convolutional Neural Networks (CNNs / ConvNets)](http://cs231n.github.io/convolutional-networks/)，中文翻译：[CS231n课程笔记翻译：卷积神经网络笔记](https://zhuanlan.zhihu.com/p/22038289)。

卷积核一般为奇数，常用的都是小卷积核，比如 1x1,3x3,5x5。[卷积](https://zh.wikipedia.org/wiki/卷积)是一种数学运算，卷积核在扫描数据的时候，正好做的就是卷积运算。卷积核其实就是个滤波器，通过平移点积运算处理数据。一个卷积层可以有多个卷积核，也就是多个滤波器，每种滤波器所『感受』的内容不同，结果也很有意思。可以看看这篇文章：[How convolutional neural networks see the world](https://blog.keras.io/how-convolutional-neural-networks-see-the-world.html)。

CNN 中不仅有 Convolution，还有 Pooling，Activation，Fully Connected等层级。

Pooling 就是 downsampling，减小数据尺寸，常用的有有 max，average 等运算。  
Activation 就是激活函数，常用的有 sigmoid，ReLU 等。  
Fully Connected 也叫 Dense，因为全连接权重密度很大。其实就是个卷积核宽高等于输入数据宽高的特殊卷积层。卷积层和全连接层可以等效转换。

如果卷积核尺寸不是 1x1，或平移的步长不是 1x1，那么卷积运算后的结果肯定比原尺寸要小，所以padding 规则就很重要。一般常用的『Same』规则就是在数据周围填充一些 0，使得卷积运算后的数据宽和高跟输入数据一样。

### [#图片分类常用的数据和预设网络模型](#图片分类常用的数据和预设网络模型)图片分类常用的数据和预设网络模型

图片分类使用已经打好标签的数据库来进行有监督学习，

| Dataset | Training Set Size | Testing Set Size | Number of Classes | Comments |
|---|---|---|---|---|
| [Cifar10](https://www.cs.toronto.edu/~kriz/cifar.html) | 60k | 10k | 10 | 32x32 color |
| [MNIST](http://yann.lecun.com/exdb/mnist/) | 60k | 10k | 10 | 28x28 gray |
| [ImageNet](http://www.image-net.org/challenges/LSVRC/2012/) | 1.2M | 50k | 1000 | Various sizes |

[MNIST](http://yann.lecun.com/exdb/mnist/) 算是深度学习领域的 HelloWorld 了。

[CIFAR](https://www.cs.toronto.edu/%7Ekriz/cifar.html) 小尺寸图片数据库，包含 CIFAR10 和 CIFAR100。

在图像识别领域，[ImageNet](http://image-net.org) 是非常有名的数据库，历年挑战中都有新的更复杂的神经网络跑出更好的结果。下面的表是一些网络模型在 [ImageNet](http://image-net.org) Challenge 中的准确率以及 TF-Slim 源码和 checkpoint 文件，数据来源：[TensorFlow-Slim image classification library](https://github.com/tensorflow/models/tree/master/slim)

| Model | TF-Slim File | Checkpoint | Top-1 Accuracy | Top-5 Accuracy |
|---|---|---|---|---|
| [Inception V1](http://arxiv.org/abs/1409.4842v1) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/inception_v1.py) | [inception_v1_2016_08_28.tar.gz](http://download.tensorflow.org/models/inception_v1_2016_08_28.tar.gz) | 69.8 | 89.6 |
| [Inception V2](http://arxiv.org/abs/1502.03167) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/inception_v2.py) | [inception_v2_2016_08_28.tar.gz](http://download.tensorflow.org/models/inception_v2_2016_08_28.tar.gz) | 73.9 | 91.8 |
| [Inception V3](http://arxiv.org/abs/1512.00567) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/inception_v3.py) | [inception_v3_2016_08_28.tar.gz](http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz) | 78.0 | 93.9 |
| [Inception V4](http://arxiv.org/abs/1602.07261) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/inception_v4.py) | [inception_v4_2016_09_09.tar.gz](http://download.tensorflow.org/models/inception_v4_2016_09_09.tar.gz) | 80.2 | 95.2 |
| [Inception-ResNet-v2](http://arxiv.org/abs/1602.07261) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/inception_resnet_v2.py) | [inception_resnet_v2.tar.gz](http://download.tensorflow.org/models/inception_resnet_v2_2016_08_30.tar.gz) | 80.4 | 95.3 |
| [ResNet V1 50](https://arxiv.org/abs/1512.03385) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/resnet_v1.py) | [resnet_v1_50.tar.gz](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz) | 75.2 | 92.2 |
| [ResNet V1 101](https://arxiv.org/abs/1512.03385) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/resnet_v1.py) | [resnet_v1_101.tar.gz](http://download.tensorflow.org/models/resnet_v1_101_2016_08_28.tar.gz) | 76.4 | 92.9 |
| [ResNet V1 152](https://arxiv.org/abs/1512.03385) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/resnet_v1.py) | [resnet_v1_152.tar.gz](http://download.tensorflow.org/models/resnet_v1_152_2016_08_28.tar.gz) | 76.8 | 93.2 |
| [ResNet V2 50](https://arxiv.org/abs/1603.05027)^ | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/resnet_v2.py) | [resnet_v2_50.tar.gz](http://download.tensorflow.org/models/resnet_v2_50_2017_04_14.tar.gz) | 75.6 | 92.8 |
| [ResNet V2 101](https://arxiv.org/abs/1603.05027)^ | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/resnet_v2.py) | [resnet_v2_101.tar.gz](http://download.tensorflow.org/models/resnet_v2_101_2017_04_14.tar.gz) | 77.0 | 93.7 |
| [ResNet V2 152](https://arxiv.org/abs/1603.05027)^ | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/resnet_v2.py) | [resnet_v2_152.tar.gz](http://download.tensorflow.org/models/resnet_v2_152_2017_04_14.tar.gz) | 77.8 | 94.1 |
| [VGG 16](http://arxiv.org/abs/1409.1556.pdf) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/vgg.py) | [vgg_16.tar.gz](http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz) | 71.5 | 89.8 |
| [VGG 19](http://arxiv.org/abs/1409.1556.pdf) | [Code](https://github.com/tensorflow/models/blob/master/slim/nets/vgg.py) | [vgg_19.tar.gz](http://download.tensorflow.org/models/vgg_19_2016_08_28.tar.gz) | 71.1 | 89.8 |

推荐一个还算不错的机器学习的数据网站：[kaggle](https://www.kaggle.com)

### [#迁移学习](#迁移学习)迁移学习

从头开始训练一个复杂的网络是很费时费力的，需要获取符合目标的海量真实数据，并使用性能极强的集群来训练数据，并有足够的耐心等待训练结果。稍有不慎，还需要不断调参，重新再来。这是个枯燥乏味的体力活，并且是在有硬件经济实力的基础上才办得到的。总会看到一些论文里描述自己的模型用 Tesla KXX 跑了多久才训练出了结果，其实在机器学习领域，花费半年甚至更久的时间来调参优化模型是很正常的。

所以基于已经训练好的模型参数来进行 fine-tuning 后应用到新的模型上是一个省时省力的方案，也被称之为迁移学习。大部分数据是存在相关性的，在图片分类问题中，即便现有模型不包含我们想要的分类，也可以利用已经训练好的权重来进行 fine-tuning，使其对新的类别进行分类。

一般的做法是将已经训练好的模型权重加载，除去 top 部分（全连接层和 softmax 分类器等），冻结前面层级的权重，只保留想要 fine-tuning 的层级（一般是后面的卷积层），最后根据分类个数自己添加全连接层。训练时只有后面的层级权重才会被修改，前面已经训练好的权重不会改变。这样会很快将正确率提高到 90% 以上。

详细内容可以参考这篇文章：([https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html))

## [#框架选择](#框架选择)框架选择

有一些知名的框架可供选择：TensorFlow, Torch, Caffee, Theano, Keras…

不同框架所使用的数据格式不一样，主要区别在于 Channel 通道的位置是在最前还是最后。框架之间的学习成本都不一样，单拿 TensorFlow 来说，其最基础的语法需要一点点构建一张图，而其 `tf.contrib.learn` 和 `tf.contrib.layers` API 是更高一层的封装，还有 TF-Slim 这种更轻量级的高级封装，几行代码就能干好多事，看起来更屌。但其实目前由于 TensorFlow 的快速迭代，导致不能向下兼容，老代码运行不起来。单拿 TF-Slim 来说，官网 API 文档缺失，Github 的教程代码老旧无法运行，还在使用从 model 库 merge 到 tensorflow 之前的语法。我当时本想用 TF-Slim 快速验证一些模型，结果没想到反而浪费了大量时间，得不偿失。

Keras 基于 TensorFlow 或 Theano，集成了大量功能，是一种方便快速验证 idea 的高层 API。 内置大量常用网络，很容易上手，语法简洁，功能强大又不失可定制性。强力推荐，官方文档：[Keras Documentation](https://keras.io)，中文文档：[Keras 中文文档](http://keras-cn.readthedocs.io/en/latest/)

无论是哪种框架，几乎都是基于分布式设计的思想，先描述出计算图，然后再向图中填充数据流，使其运转起来，最后得到结果。虽然是使用 Python 语言来描述计算图，但是真正繁重的工作都会提交给底层的后端去处理。但这样也给 debug 带来了困难，因为描述计算图的时候并不能得到数据结果，只能检查出数据格式是否匹配。

> 笼统的说，符号主义的计算首先定义各种变量，然后建立一个“计算图”，计算图规定了各个变量之间的计算关系。建立好的计算图需要编译以确定其内部细节，然而，此时的计算图还是一个“空壳子”，里面没有任何实际的数据，只有当你把需要运算的输入放进去后，才能在整个模型中形成数据流，从而形成输出值。  
>  就像用管道搭建供水系统，当你在拼水管的时候，里面是没有水的。只有所有的管子都接完了，才能送水。  
>  – 引自 [http://keras-cn.readthedocs.io/en/latest/for_beginners/concepts/](http://keras-cn.readthedocs.io/en/latest/for_beginners/concepts/)

## [#数据采集](#数据采集)数据采集

因为网上提供的一些用于训练的海量图片数据都是格式整齐像素较低的图片，比如28x28这种，且特征明显，都为某种物体，这种专用于比赛挑战的图片分类数量一般都是10，100，1000等，更专注于算法的准确率，忽视了真实的场景。

为了模拟真实场景，我使用 Web 程序调用 iMac 前置摄像头采集 320x240 尺寸的照片。为了更高效采集图片数据，我采用连拍的方式拍摄并保存图片到本地：

![帅是我的无奈](http://yulingtianxia.com/resources/MachineLearning/training_data.png)

需要去除少量过于模糊和手指不小心跑出屏幕外的图片，尽可能提高数据的质量。

因为不同平台和浏览器对 Html5 规范支持程度不同，建议在 Mac 上使用 Firefox，Windows 上应该 Chrome 也好使，但没试过。

图像采集的代码放在 [captureImages](https://github.com/yulingtianxia/HandGestureCNN/tree/master/captureImages) 目录里。

## [#Inception-V3-pre-trained-network](#Inception-V3-pre-trained-network)Inception V3 pre-trained network

在 Keras Blog 中，[Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html) 很好地介绍了如何针对小数据集利用现有的 VGG16 网络 fine-tuning，并在 [Dogs vs. Cats](https://www.kaggle.com/c/dogs-vs-cats/data) 数据集上取得了 94% 的准确率。

VGG 系列网络虽然结构简单易理解，但无论是加载权重的耗时还是预测耗时都要比 Inception 系列网络要长，这是因为其权重数据更多。虽然 Inception 系列更复杂，但鉴于其优秀的性能和更胜一筹的准确率，我决定在移动设备上使用 Inception 而非 VGG。

其实苹果爸爸已经帮我们用 Swift 和 Metal Performance Shaders 实现了个使用 Inception V3 网络预测图像类别的 Demo:[MetalImageRecognition: Performing Image Recognition with Inception_v3 Network using Metal Performance Shaders Convolutional Neural Network routines](https://developer.apple.com/library/content/samplecode/MetalImageRecognition/Introduction/Intro.html)

所以我决定使用 [Inception V3 Network](https://arxiv.org/pdf/1512.00567v3.pdf) 来 fine-tuning，这样在后续的 MPS 代码编写上就会省很多时间。TensorFlow 官方也有相应 [教程](https://www.tensorflow.org/tutorials/image_recognition#image-recognition)。

### [#bottleneck-features](#bottleneck-features)bottleneck features

下图展示了 Inception V3 网络的结构，其中的 top 部分就是 Final part 所指的部分，我们可以将其替换成我们自己的全连接层，利用前面 Input 预测的结果来作为输入数据，训练我们自己的分类器。

![]([http://yulingtianxia.com/resources/MachineLearning/Inception](http://yulingtianxia.com/resources/MachineLearning/Inception) V3.png)

> 上图中的 Inception mudules 使用的是[论文](https://arxiv.org/pdf/1512.00567v3.pdf)中提到的图 6 的结构，实际代码中则使用的图 5。

Keras 有很多使用 ImageNet 预训练的模型，我们这里只需要 Inception V3 去掉 Final part 的剩余部分，一行代码搞定：

```routeros
model = applications.InceptionV3(include_top=False, weights='imagenet')
```

在 TensorFlow 中读取文件数据需要通过 `QueueRunner` 和 `Coordinator` 构造队列来实现 data flow，比较麻烦：

![图片来源 TensorFlow](http://yulingtianxia.com/resources/MachineLearning/AnimatedFileQueues.gif)

Keras 真是太方便了，用生成器把图片数据标准化，使用加载好的 `model` 预测出结果，并保存到 npy 文件中。

```nix
datagen = ImageDataGenerator(rescale=1. / 255)
generator = datagen.flow_from_directory(
   train_data_dir,
   target_size=(img_width, img_height),
   batch_size=batch_size,
   class_mode=None,
   shuffle=False)
bottleneck_features_train = model.predict_generator(
   generator, nb_train_samples // batch_size)
np.save(open('bottleneck_features_train.npy', 'w'),
       bottleneck_features_train)
```

这里保存的结果并不是 one-hot 格式的分类结果，只是作为 Final part 的输入，所以叫做 bottleneck features。

下一步就是构建自己的 Final part，比如我们这里想要做个五分类的模型：

```routeros
model = Sequential()
model.add(Flatten(input_shape=train_data.shape[1:]))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))
```

`Flatten` 和 `Dropout` 层并不会改变数据，是没有权重的层。所以这里有两个全连接层，最后一层有五个节点，输出一个长度为 5 的 one-hot 格式向量。

这里之所以使用 bottleneck features 作为输入数据来进行训练，是为了节省运算资源。如果采用冻结前面部分网络的方式，虽然被冻结的网络权重不会变，但每跑一次的运算量都很大，而且结果是相同的。所以采取预测一次 bottleneck features，离线保存的方式。在机器学习中减少 loss 提升准确率常用的方法就是梯度下降法，实际应用中使用 mini-batch 梯度下降法来平衡计算性能和 loss 收敛效果。这里的 batch_size 就是每次下降所使用数据批次的数量。

```routeros
model.compile(optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
             loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_data, train_labels,
         epochs=epochs,
         batch_size=batch_size,
         validation_data=(validation_data, validation_labels))
model.save_weights(top_model_weights_path)
```

这里训练的是我们自己添加的两个全连接层，以便于拟合我们自己的数据。

这部分的源码放在 [bottleneck_features_train_inceptionv3.py](https://github.com/yulingtianxia/HandGestureCNN/blob/master/Train/bottleneck_features_train_inceptionv3.py)

### [#Fine-tuning](#Fine-tuning)Fine-tuning

为了达到更好的效果，可以解冻后面几层。看了下 Inception V3 的网络结构，最后一个 tower 拥有 9 个卷积层，比较复杂。虽然理论上 fine-tuneing 整个 tower 是可行的，但是计算开销很大，用我的 iMac 4 GHz Intel Core i7 八核跑一个月都不行。

现在需要加载预训练网络的权重到 `base_model` 中，并将其与 `top_model` 拼在一起。Keras 中有两种描述模型，一种是 `Sequential`，另一种是带有函数式 API 的 `Model`。前者层与层之前连接的入度和出度都为 1，后者就很灵活很随意了。这里构建 `top_model` 使用的 `Sequential`，然后使用 `Model` 统一输入和输出，起到连接的作用。最后通过设置 `trainable` 属性来冻结部分网络。为了让准确率更高，会将上一步 bottleneck features 训练好的权重作为 `top_model` 的初始权重。

```routeros
# build the InceptionV3 network
input_tensor = Input(shape=(img_height, img_width, 3))
base_model = applications.InceptionV3(weights='imagenet', include_top=False, input_tensor=input_tensor)
print('Model loaded.')

# build a classifier model to put on top of the convolutional model
top_model = Sequential()
top_model.add(Flatten(input_shape=base_model.output_shape[1:]))
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(5, activation='softmax'))

# note that it is necessary to start with a fully-trained
# classifier, including the top classifier,
# in order to successfully do fine-tuning
top_model.load_weights(top_model_weights_path)

# add the model on top of the convolutional base
model = Model(inputs=base_model.input, outputs=top_model(base_model.output))

# set the first xx layers (up to the last conv block)
# to non-trainable (weights will not be updated)

for layer in model.layers[:len(base_model.layers)-5]:
    layer.trainable = False
```

有关 Keras 两种模型的概念可以查看 [About Keras models](https://keras.io/models/about-keras-models/)。

可以通过设置数据生成器的一些参数来提升数据的随机性，降低过拟合。`ImageDataGenerator` 针对图片有很多预设的处理方式，例如平移，旋转，缩放，反转等。TensorFlow 中也有类似的图片预处理功能，但 API 使用上没 Keras 便利。有关图片预处理的内容可以参考文档 [Image Preprocessing](https://keras.io/preprocessing/image/)，这里仅针对某些方式进行随意预处理，提升数据：

```routeros
train_datagen = ImageDataGenerator(
	rescale=1./255,
  	rotation_range=40,
  	width_shift_range=0.2,
  	height_shift_range=0.2,
  	shear_range=0.2,
  	zoom_range=0.2,
  	horizontal_flip=True,
  	fill_mode='nearest')
```

Keras 可以根据数据的文件夹自动分类打标签，所以我将图片按文件夹归类就可以了，很方便。

我一共使用了 1808 张图片作为训练集，192 张图片作为交叉验证集。经过了 50 个 epoch 后，训练集准确率 96.26%，交叉验证集准确率 73.86%。

这部分源码放在 [finetune_inceptionv3.py](https://github.com/yulingtianxia/HandGestureCNN/blob/master/Train/finetune_inceptionv3.py)

## [#Convert-HDF5-to-binary-dat-files](#Convert-HDF5-to-binary-dat-files)Convert HDF5 to binary .dat files

> HDF（英语：Hierarchical Data Format）指一种为存储和处理大容量科学数据设计的文件格式及相应库文件。HDF最早由NCSA开发，目前在非盈利组织 HDF 小组维护下继续发展。当前流行的版本是HDF5。  
>  – 维基百科

[HDF Group](https://www.hdfgroup.org) 提供了可视化查看 HDF 文件的工具：[HDFView](https://support.hdfgroup.org/products/java/release/download.html)，因为是用 java 写的，所以是跨平台的。Mac 版本有个已知的 bug：双击一个 `.h5` 文件后 HDFView 界面是空的，需要把 `.h5` 文件拖动到 HDFView 左边栏才能打开。

![](http://yulingtianxia.com/resources/MachineLearning/HDFView.jpg)

Keras 可以将训练处的权重结果高存成 HDF5 格式，但苹果提供的 Demo 使用的权重文件是 memory-mapped 二进制文件，每层网络都对应一个 `.dat` 文件。

[SOFTWARE USING HDF5](https://support.hdfgroup.org/products/hdf5_tools/index.html) 列举了很多用于操作 HDF 文件和格式转换的工具。可以用一些工具将存有权重的 HDF 文件先转化成若干 `.dat` 文件，然后再打包到 iOS App 中。还有一种做法是将 HDF 文件打包到 iOS App 中，然后在客户端完成格式导出。[HDF5Kit](https://github.com/aleph7/HDF5Kit) 是对 [HDF 源码](https://support.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/)的 Swift 封装，不过还有些 crash。我采用了第二种做法，因为我懒，替换权重文件的时候只需要一个 HDF 文件，不用替换一堆 `.dat` 文件🙄。实际应用中千万别这么干。

可以根据上图中 HDFView 展示的树状层级递归遍历 Group，并拼接好正确的名称。比如 “bias:0” 和 “kernel:0”。将 HDF5 转换成二进制文件的代码如下：

```swift
// Read parameters from HDF5 file and store to dat file in Tmp directory
func extractHDF5(h5Name: String) {
    // MARK: Parse HDF5 file
    guard let path = Bundle.main.path(forResource: h5Name, ofType: "h5") else {
        fatalError("Failed to get a path")
    }
    guard let file = File.open(path, mode: .readOnly) else {
        fatalError("Failed to open file at \(path)")
    }

    guard let layerNamesStringAttribute = file.openStringAttribute("layer_names") else {
        fatalError("Failed to open attribute 'layer_names'")
    }
    guard let layerNames = try? layerNamesStringAttribute.read() else {
        fatalError("Failed to get layer names")
    }

    // count used for file name later
    var countOfConvLayer = 0
    var countOfFcLayer   = 0
    var partOfFileName = ""

    for layerName in layerNames {
        guard let layerGroup = file.openGroup(layerName) else {
            fatalError("Failed to open group of \(layerName)")
        }
        for objectName in layerGroup.objectNames() {

            // only the layer that has parameters remain
            guard let wtDataset = layerGroup.openFloatDataset(objectName + "/kernel:0") else {
                fatalError("Failed to open data set of \(objectName)/kernel:0")
            }
            guard let bsDataset = layerGroup.openFloatDataset(objectName + "/bias:0") else {
                fatalError("Failed to open data set of \(objectName)/bias:0")
            }

            var dimension = wtDataset.space.dims
            guard var wtArray = try? wtDataset.read() else {
                fatalError("Failed to read data set of \(objectName)/kernel:0")
            }
            guard var bsArray = try? bsDataset.read() else {
                fatalError("Failed to read data set of \(objectName)/bias:0")
            }

            let wtLength = wtArray.count
            let bsLength = bsArray.count

            if dimension.count == 4 {
                // weights for convolution layer
                wtArray = SwapAxes.for4dFlatArray(originalArray: wtArray, axis1: 2, axis2: 3, dimensionOfArray: &dimension)
                wtArray = SwapAxes.for4dFlatArray(originalArray: wtArray, axis1: 1, axis2: 2, dimensionOfArray: &dimension)
                wtArray = SwapAxes.for4dFlatArray(originalArray: wtArray, axis1: 0, axis2: 1, dimensionOfArray: &dimension)

                countOfConvLayer += 1
                partOfFileName = "conv" + String(countOfConvLayer)

            } else if dimension.count == 2 {
                // weights for fully connected layer
                wtArray = SwapAxes.for2dFlatArray(originalArray: wtArray, axis1: 0, axis2: 1, dimensionOfArray: &dimension)

                countOfFcLayer += 1
                partOfFileName = "fc" + String(countOfFcLayer)

            } else {
                fatalError("Dataset's dimension is neither 4 (convolution layer) nor 2 (fully connected layer)")
            }

            let wtData = NSData(bytes: &wtArray, length: wtLength * MemoryLayout<Float>.size)
            let bsData = NSData(bytes: &bsArray, length: bsLength * MemoryLayout<Float>.size)

            // 写入数据到文件...
        }
    }
}
```

## [#Metal-Performance-Shaders](#Metal-Performance-Shaders)Metal Performance Shaders

### [#MPS-简介](#MPS-简介)MPS 简介

Metal Performance Shaders 简称 MPS，可以为使用 Metal 技术的 App 提供底层高性能 GPU 运算接口。最初苹果提供的 Shader 语言本来是很底层很生涩的，后来为 iOS 提供了原生支持的 API，可以用 Swift 或 OC 来调用底层接口了。iOS 9 的 MPS 提供了图片特效处理和 Metal 纹理相关的 API，iOS 10 的 MPS 新增了有关 CNN 和矩阵乘法的 API。不过目前苹果只开放了 CNN 的预测功能，如果想要在 iOS 10 上训练一个 CNN，那就只能借助第三方工具了。

苹果的 BNNS 同样提供了创建 CNN 的 API，而且也只能使用训练好的权重进行预测。但仅仅是对 CPU 进行了优化。因为 OpenGL 的限制，其性能与 Metal 相比并不占优势。OpenCL 在 iOS 上是私有框架。所以说目前看来，不考虑系统兼容性(iOS 10)和资源限制(arm64)，Metal 技术是发挥 GPU 运算优势的最好选择。

MPS 系统原生支持不用担心安装包增量问题，并且使用 Metal 技术使用 GPU 加速运算，功耗发热少。MPS 目前的缺点是不支持网络的训练和必须 HardCode 网络结构，但面对复杂度较低的神经网络时还是很实用的。毕竟 TensorFlow 在 iOS 上只能用 CPU 计算，且编译费时费力，安装包增量巨大。

MPS 在我的 iPhone 6s Plus 上性能很好，发热也少，可以通过神经网络实时预测出结果。这是 [iOS-10-Sampler](https://github.com/shu223/iOS-10-Sampler) 项目的效果，它是在苹果官方 Demo [MetalImageRecognition](https://developer.apple.com/library/content/samplecode/MetalImageRecognition/Introduction/Intro.html) 基础上稍微改进拍摄功能的用户体验，MPS 的部分未做任何改动。我基于它和 [MPSCNNfeeder](https://github.com/kazoo-kmt/MPSCNNfeeder) 实现了 [HandGestureCNN](https://github.com/yulingtianxia/HandGestureCNN/tree/master/HandGestureCNN)。

![](https://github.com/shu223/iOS-10-Sampler/blob/master/README_resources/imagerecog.gif?raw=true)

苹果给了一个 MPS 的 HelloWorld： [MPSCNNHelloWorld: Simple Digit Detection Convolution Neural Networks (CNN)](https://developer.apple.com/library/content/samplecode/MPSCNNHelloWorld/Introduction/Intro.html)，恰好对应着机器学习领域的 HelloWorld MNIST。可以通过查看这个 Demo 的源码来快速上手 MPS 的用法。

其实总体来说并不是很复杂，但有几个重要的地方需要我们自己去解决：

1. 数据处理，也就是模型文件的数据格式需要自己去解析。不同深度学习框架导出的模型权重文件格式都不一样，会涉及到比较底层的位读写。这里有一定工作量。
2. 使用卷积神经网络预测模型的时候，会涉及到 padding，这部分需要自己计算。输出数据体在空间上的尺寸可以通过输入数据体尺寸（W），卷积层中神经元的感受野尺寸（F），步长（S）和零填充的数量（P）的函数来计算。输出数据体的空间尺寸为 (W-F +2P)/S+1。这里说的是某个维度，单指宽或长。
3. `MPSImage` 是为了突破 `MTLTexture` 最大维度为 4 （RGBA）的限制，搞了个 workaround，就是用多个切片模拟多维度。如果有 N 个维度，那么切片数量为 (N+3)/4。比如下图为 N = 9 的情况。所以涉及到数据对齐的事情，预测后的数据需要处理下。

  ![](https://docs-assets.developer.apple.com/published/48ad0af3fd/b6d1d091-162c-418d-bc2e-0b6f3105c126.png)

好在苹果提供的 Demo 里已经对于后两个问题有了可以参考的代码，第一个问题其实是个矩阵转换的操作。 TensorFlow 卷积核权重的顺序为 [kH kW iC oC]，而 MPS 接受的权重为 [oC kH kW iC] 形式。而我使用 Keras 的时候将 TensorFlow 作为后端，所以需要转换下权重格式。矩阵转换在 python 里很容易，还好我找到了 Swift 版本的实现：[SwapAxes](https://github.com/kazoo-kmt/MPSCNNfeeder/blob/master/swapaxes.swift)，直接拿过来用了。

> PS: 科普下，[oC kH kW iC] 是四维数组（矩阵） [outputChannels][kernelHeight][kernelWidth][inputChannels/groups] 的 shape。

### [#使用-MPS-构建网络并预测](#使用-MPS-构建网络并预测)使用 MPS 构建网络并预测

MPS 预测的执行流程如下：

1. 获取可用的 device
2. 获取

  ，从

  获取
3. 对象
4. 方法，输入为

  和上一层网络输出的

  对象。
5. 提交 `commandBuffer`
6. 等待输出结果，并处理成 one-hot 格式。

剩下的工作就是修改工程中的 `Inception3Net.swift` 文件，使其网络结构与我们用 Keras 搭建的网络结构一样即可。前面提到过，`Flatten` 和 `Dropout` 没有权重，不改变数据。`Flatten` 其实就是 `reshape` 操作，在 MPS 中不需要特意做 `reshape` 操作也没有 `Flatten` 层，`MPSImage` 被描述成什么 shape，数据就会被排列成那个 shape。`Dropout` 层在训练的时候按一定几率丢弃结果，在预测模型的时候根本用不到。

回顾下之前用 Keras 写的全连接层结构的代码：

```routeros
model = Sequential()
model.add(Flatten(input_shape=train_data.shape[1:]))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(5, activation='softmax'))
```

转换成 MPS 的代码后差不多是这个样子（省略无关代码）：

```groovy
let device = inputCommandQueue.device
let relu = MPSCNNNeuronReLU(device: device!, a: 0)
let softmax = MPSCNNSoftMax(device: device!)
let sftid = MPSImageDescriptor(channelFormat: textureFormat, width: 1  , height: 1  , featureChannels: 5)
// logits
let fc0 = SlimMPSCNNFullyConnected(kernelWidth: 8,
                             kernelHeight: 8,
                             inputFeatureChannels: 2048,
                             outputFeatureChannels: 256,
                             neuronFilter: relu,
                             device: device,
                             kernelParamsBinaryName: "fc1")

let fc1 = SlimMPSCNNFullyConnected(kernelWidth: 1,
                             kernelHeight: 1,
                             inputFeatureChannels: 256,
                             outputFeatureChannels: 5,
                             neuronFilter: nil,
                             device: device,
                             kernelParamsBinaryName: "fc2")
...
let image10 = ...
let sftImage    = MPSImage(device: device!, imageDescriptor: sftid)

...

// MPSImageDescriptor for final logits generating layers
let fc0id = MPSImageDescriptor(channelFormat: textureFormat, width: 1, height: 1, featureChannels: 256)

var fc0Image, fc1Image : MPSTemporaryImage!

func logits_layer(commandBuffer: MTLCommandBuffer){
   // These images are only needed in this layer and will not be read by the CPU or
   // outside of the command bufer, so we can allocate them as MPSTemporaryImages and
   // save the CPU cost and memory size of allocating reserved storage for them.
   //
   // These objects can not be reused outside of the command buffer, which is why
   // we did not make them in the init(withDevice:commandQueue:) call.
   //
   // Temporary images are designed to be efficiently created as needed, used a few times
   // and thrown away almost immediately

   fc0Image     = MPSTemporaryImage(commandBuffer: commandBuffer, imageDescriptor: fc0id)
   fc1Image     = MPSTemporaryImage(commandBuffer: commandBuffer, imageDescriptor: sftid)

   // encode layers to metal commandBuffer
   fc0.encode    (commandBuffer: commandBuffer, sourceImage: image10, destinationImage: fc0Image)
   fc1.encode    (commandBuffer: commandBuffer, sourceImage: fc0Image, destinationImage: fc1Image)
   softmax.encode(commandBuffer: commandBuffer, sourceImage: fc1Image, destinationImage: sftImage)

}
```

## [#总结](#总结)总结

这是一篇行外人看不懂，行内人觉得水，我自己觉得收获满满的实践笔记。并没有花大量篇幅总结Machine Learning 的基础知识，也没有逐个讲述框架 API 的使用，更没有列一堆公式和数学定义。。。因为这种知识体系大而全的文章，网上不胜枚举，而且肯定比我总结的好。本着一个小白去探索世界的心态，把自己从理论学习到训练模型再到 iOS 上的预测的实践流程记录下来。很多枯燥耗时的学习 ML、TF 和配置环境的过程都省略掉了。

最后建议如果有条件的话，还是用配置较高的集群或者云服务来训练模型，节省程序员宝贵的时间。如果不能做到自己提出创新有效的网络模型，其实深度学习的大量工作就是调参、采集数据、看别人论文如何改参数和网络结构，然后等待机器训练结果。。。反复循环。。。

神经网络不是真的模拟出人脑的生物特征，CNN 跟人眼扫视世界或人脑辨别物体其实差很多，深度学习只是尽力让机器拟合出想要的结果罢了，离真正的人工智能还差远了。所以不要被铺天盖地的吹嘘洗脑了，一个 AlphaGo 就能又让一大堆所谓的科技媒体高潮出机器快要统治人类了，不要老想搞个大新闻！

深度学习发展很快，要学习的内容还有很多。学习得越多，就发现自己越是无知，以至于怀疑自己的智商和精力了。

## [#Reference](#Reference)Reference

[Coursera Machine Learning](https://www.coursera.org/learn/machine-learning/home)  
[TensorFlow](https://www.tensorflow.org)  
[Keras 中文文档](http://keras-cn.readthedocs.io/en/latest/)  
[Keras Documentation](https://keras.io)  
[ImageNet](http://image-net.org)  
[kaggle](https://www.kaggle.com)  
[CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.stanford.edu)  
[Convolutional Neural Networks (CNNs / ConvNets)](http://cs231n.github.io/convolutional-networks/)  
[Convolutional neural networks on the iPhone with VGGNet](http://machinethink.net/blog/convolutional-neural-networks-on-the-iphone-with-vggnet/)  
[Building powerful image classification models using very little data](https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html)  
[HDF Group](https://www.hdfgroup.org)  
[MetalPerformanceShaders](https://developer.apple.com/reference/metalperformanceshaders)  
[BNNS](https://developer.apple.com/reference/accelerate/bnns)  
[HDF5Kit](https://github.com/aleph7/HDF5Kit)  
[iOS-10-Sampler](https://github.com/shu223/iOS-10-Sampler)  
[MPSCNNfeeder](https://github.com/kazoo-kmt/MPSCNNfeeder)
