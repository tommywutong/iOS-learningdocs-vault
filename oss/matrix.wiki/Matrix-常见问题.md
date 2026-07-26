## Issue /提问须知
**在提交issue之前，我们应该先查询是否已经有相关的 issue 以及[常见问题](https://github.com/tencent/matrix/wiki/Matrix-%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)。提交 issue 时，我们需要写明 issue 的原因，以及编译或运行过程的日志。issue 需要以下面的格式：**

```
异常类型：app 运行时异常/编译异常

手机型号：如: Nexus 5(如是编译异常，则可以不填)

手机系统版本：如: Android 5.0 (如是编译异常，则可以不填)

matrix版本：如: 0.4.8

gradle版本：如: 3.0.0

问题描述：简述你遇到了什么问题

堆栈/日志：
1. 如是编译异常，请在执行 gradle 命令时，加上 --stacktrace;
2. 日志我们需要过滤 "Matrix." 关键字;
```

提问题时若使用`不能用/没效果/有问题/报错`此类模糊表达，但又没给出任何代码截图报错的，将绝对不会有任何反馈。这种 issue 也是一律直接关闭的,大家可以参阅[提问的智慧](https://github.com/tvvocold/How-To-Ask-Questions-The-Smart-Way)。

Matrix 是一个开源项目，希望大家遇到问题时要学会先思考，看看 Sample 与 Matrix 的源码，更鼓励大家给我们提 pr .

## Matrix 常见问题
1. 支持哪些平台？   

    当前主要是 android 平台，即将发布ios和mac平台的版本，敬请期待。

2. ResourceCanary InputMethodManager 误报问题 

    由于部分 ROM 的 InputMethodManager 中存在一个 Context 成员变量会持有当前 Activity，且 InputMethodManager 是一个全局单例，因此会导致 ResourceCanary 在这些 ROM 上产生误报。实际使用时需要在后台分析过程中，根据分析出来的引用链（引用链中含有 InputMethodManager）过滤掉这类误报。

3. 模拟器中点击 “IO_CANARY" 出现 “signal 31 (SIGSYS), code 1 (SYS_SECCOMP)” crash

   IO 检测方案中使用了 elf_hook，在 x86 环境中相关 API 被禁用，请在真机中测试使用。

4. Matrix 上报到哪里呢？有没有网站可以查看到?

   当前matrix只是作为性能探针插件提供，无对外的管理后台服务。 数据上报的内容可以通过继承DefaultPluginListener来获取。
而evilmethod的堆栈反解，在sample中有例子可查([issue#104](https://github.com/Tencent/matrix/issues/104))