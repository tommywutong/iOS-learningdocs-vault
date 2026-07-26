---
title: 实现一个TODO宏 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2015/03/01/todo-macro/'
original_language: zh
published: 2015-03-01
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4e36c34447718a05'
translated: n/a
---

> 原文：[实现一个TODO宏 · sunnyxx的技术博客](http://blog.sunnyxx.com/2015/03/01/todo-macro/)　·　sunnyxx (孙源)

# 实现一个TODO宏

2015年3月1日

实现一个能产生warning的TODO宏，用于在代码里做备忘，效果：

![](http://ww1.sinaimg.cn/large/51530583jw1eprfhhfis1j20w004mju0.jpg)  
![](http://ww3.sinaimg.cn/large/51530583jw1eprfhhspaqj20nu0bqae6.jpg)

下面一步步来实现这个宏。

---

# Let’s do it

手动让编译器报警（报错）可以用以下几个方法：

```objc
#warning sunnyxx
#error sunnyxx
#pragma message "sunnyxx"
#pragma GCC warning "sunnyxx"
#pragma GCC error "sunnyxx"
```

但我们知道，带`#`的预处理指令是无法被`#define`的。好在**C99**提供了一个`_Pragma`运算符可以把部分`#pragma`指令字符串化：

```objc
#pragma message "sunnyxx"
// 等价于
_Pragma("message \"sunnyxx\"") // 需要注意双引号的转义
// 或
_Pragma("message(\"sunnyxx\")") // 需要注意双引号的转义
```

利用这个特性，我们就可以将warning定义成宏

```objc
#define SOME_WARNING _Pragma("message(\"报告大王！\")")
int main() {
    SOME_WARNING // [!]报告大王！
    return 1;
}
```

接下来，我们让这个宏能够接受入参，并显示到warning中去，这里会面临宏的基本用法的考验。

```objc
#define STRINGIFY(S) #S
#define PRAGMA_MESSAGE(MSG) _Pragma(STRINGIFY(message(MSG)))
```

个人认为不太可能在一个宏定义中完成这件事，需要用到辅助宏：`STRINGIFY(S)` 将入参转化成字符串，省去了`_Pragma`中全串加转义字符的困扰。  
这时，一个基本功能的TODO宏就完成了，下面向其中加入**额外的信息**：

```objc
// 两个已有的宏
#define STRINGIFY(S) #S
#define PRAGMA_MESSAGE(MSG) _Pragma(STRINGIFY(message(MSG)))
// 延迟1次展开的宏
#define DEFER_STRINGIFY(S) STRINGIFY(S)
// 下面的宏在第一行用`\`折行
#define FORMATTED_MESSAGE(MSG) "[TODO-" DEFER_STRINGIFY(__COUNTER__) "] " MSG " \n"  \
    DEFER_STRINGIFY(__FILE__) " line " DEFER_STRINGIFY(__LINE__)
```

其中涉及到的知识：

- 两个常量字符串可以拼接成一个整串 “123””456” =\> “123456”
- 使用到3个**预定义宏**，`__COUNTER__`宏展开次数的计数器，全局唯一；`__FILE__`当前文件完整目录字符串；`__LINE__`在当前文件第几行
- 在字符串中**预定义宏**应延时展开，如果将上面的`DEFER_STRINGIFY`换成`STRINGIFY`的话，如`__LINE__`就不能被正确展开成行数，而是成了一个常量字符串`"__LINE__"`
- 为了美化，warning message中可以使用`\n`换行

于是，使用`FORMATTED_MESSAGE(MSG)`宏就可以将带文件路径、序号、行数等信息加入到最终的warning中。

---

其实到这步已经OK了，为了让这个宏更加抢眼，还可以借鉴RAC，把宏定义成前面加`@`的形式：

```objc
#define KEYWORDIFY try {} @catch (...) {}
```

将最终的宏定义前面加上上面的宏后，使用时就可以加`@`前缀了（空的try-catch会被编译器优化，所以没啥性能损耗）

---

# 最终版本

```objc
#define STRINGIFY(S) #S
#define DEFER_STRINGIFY(S) STRINGIFY(S)
#define PRAGMA_MESSAGE(MSG) _Pragma(STRINGIFY(message(MSG)))
#define FORMATTED_MESSAGE(MSG) "[TODO-" DEFER_STRINGIFY(__COUNTER__) "] " MSG " \n" \
DEFER_STRINGIFY(__FILE__) " line " DEFER_STRINGIFY(__LINE__)
#define KEYWORDIFY try {} @catch (...) {}
// 最终使用下面的宏
#define TODO(MSG) KEYWORDIFY PRAGMA_MESSAGE(FORMATTED_MESSAGE(MSG))
```

---

# What’s more

除此之外，还研究了半天如何在宏里面定义一个注释，这样就可以偷偷写`// TODO: ...`的注释，让Xcode导航栏中也出现这个TODO了：  
![](http://ww4.sinaimg.cn/large/51530583jw1eprhben4m9j20by02oglq.jpg)  
但很可惜没有找到一个可行的方法，欢迎一起解决。  
Xcode插件[《XTodo》](https://github.com/trawor/XToDo)也是利用这个特性，可以尝试下。

如果需要一个产生error的宏，将这里替换成这样就好了：`_Pragma(STRINGIFY(GCC error(MSG)))`

同时，上面的代码在[《github上》](https://github.com/sunnyxx/TodoMacro)可以找到。也欢迎关注微博[@我就叫Sunny怎么了](http://weibo.com/u/1364395395)一起交流。

# References

[http://clang.llvm.org/docs/UsersManual.html](http://clang.llvm.org/docs/UsersManual.html)  
[https://gcc.gnu.org/onlinedocs/cpp/Pragmas.html](https://gcc.gnu.org/onlinedocs/cpp/Pragmas.html)
