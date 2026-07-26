# 学习计划 · 材料索引

> 由 `tools/studyplan.py` 从 `2026 暑假 iOS 底层学习计划.md` 自动生成。
> 每一行是计划里点名的一份材料；有本地归档的给出链接，没有的标「未归档」。

## 覆盖率

| 类别 | 链接数 | 已归档 | 覆盖率 |
|---|---:|---:|---:|
| 第三方博客 | 223 | 39 | 17% |
| Apple 现行文档 | 43 | 3 | 7% |
| GitHub 源码 | 35 | 0 | 0% |
| Apple 旧归档 | 30 | 0 | 0% |
| WWDC | 6 | 6 | 100% |
| Apple 其它 | 1 | 0 | 0% |


## 第一周：对象、类与所有权的地基

### Day 1｜先分清“地址空间”，不要一上来背 isa（对应 W1-10）

- [原文](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/vm/vm.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [本地](blogs/en/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html) — 第三方博客
- [本地](blogs/en/alwaysprocessing/size-matters-an-exploration-of-virtual-memory-on-ios-an-out-of-memory-crash-while-debuggin.md) · [原文](https://alwaysprocessing.blog/2022/02/20/size-matters) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2010-01-15-stack-and-heap-objects-in-objective-c.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2010-01-15-stack-and-heap-objects-in-objective-c.html) — 第三方博客
- [原文](https://juejin.cn/post/6963188936508178469) — 第三方博客（未归档（juejin.cn））
### Day 2｜从一个对象逐层走到元类（对应 W1-01、W1-04）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [本地](wwdc/en/wwdc2020/10163-advancements-in-the-objective-c-runtime.md) · [原文](https://developer.apple.com/videos/play/wwdc2020/10163/) — WWDC
- [本地](blogs/en/alwaysprocessing/objective-c-internals-class-architecture-objective-c-has-an-unique-class-architecture-wher.md) · [原文](https://alwaysprocessing.blog/2023/01/02/objc-class-arch) — 第三方博客
- [本地](blogs/en/alwaysprocessing/objective-c-internals-class-graph-implementation-a-brief-look-at-the-objective-c-runtime-s.md) · [原文](https://alwaysprocessing.blog/2023/01/10/objc-class-graph-impl) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html) — 第三方博客
- [原文](https://draven.co/isa/) — 第三方博客（未归档（draven.co））
- [原文](https://blog.devtang.com/2013/10/15/objective-c-object-model/) — 第三方博客（未归档（blog.devtang.com））
- [本地](blogs/en/cocoawithlove/what-is-a-meta-class-in-objective-c-cocoa-with-love.md) · [原文](https://www.cocoawithlove.com/2010/01/what-is-meta-class-in-objective-c.html) — 第三方博客
- [本地](blogs/en/mikeash/previous.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2014-07-18-exploring-swift-memory-layout.html) — 第三方博客
- [本地](blogs/en/sealiesoftware/objc-explain-non-pointer-isa.md) · [原文](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) — 第三方博客
- [原文](https://github.com/apple-oss-distributions/objc4) — GitHub 源码（待 clone 到 oss/）
### Day 3｜在结构图上推导类型判断，再看 Tagged Pointer（对应 W1-05、W1-06）

- [原文](https://developer.apple.com/documentation/objectivec/nsobject) — Apple 现行文档（未归档）
- [本地](blogs/en/alwaysprocessing/objective-c-internals-the-many-uses-of-isa-the-objective-c-runtime-optimizes-performance-b.md) · [原文](https://alwaysprocessing.blog/2023/01/19/objc-class-isa) — 第三方博客
- [原文](https://www.cnblogs.com/xgao/p/11277935.html) — 第三方博客（未归档（cnblogs.com））
- [原文](https://www.0daybug.com/posts/9972ffa7/index.html) — 第三方博客（未归档（0daybug.com））
- [原文](https://roadmap.isylar.com/iOS/Knowledge/RuntimeCls.html) — 第三方博客（未归档（roadmap.isylar.com））
- [本地](wwdc/en/wwdc2020/10163-advancements-in-the-objective-c-runtime.md) · [原文](https://developer.apple.com/videos/play/wwdc2020/10163/) — WWDC
- [原文](https://clang.llvm.org/docs/AttributeReference.html#aligned) — 第三方博客（未归档（clang.llvm.org））
- [本地](blogs/en/alwaysprocessing/objective-c-internals-tagged-pointer-objects-tagged-pointer-objects-a-private-runtime-feat.md) · [原文](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr) — 第三方博客
- [本地](blogs/en/mikeash/tagged-pointers.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2015-07-31-tagged-pointer-strings.md) · [原文](https://mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html) — 第三方博客
- [原文](https://blog.devtang.com/2014/05/30/understand-tagged-pointer/) — 第三方博客（未归档（blog.devtang.com））
- [原文](https://blog.timac.org/2016/1124-testing-if-an-arbitrary-pointer-is-a-valid-objective-c-object/) — 第三方博客（未归档（blog.timac.org））
### Day 4｜先用 MRC 学所有权规则，再看 ARC（对应 W1-02）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://clang.llvm.org/docs/AutomaticReferenceCounting.html) — 第三方博客（未归档（clang.llvm.org））
- [本地](blogs/en/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md) · [原文](https://alwaysprocessing.blog/2023/07/22/objc-retain) — 第三方博客
- [原文](https://draven.co/rr/) — 第三方博客（未归档（draven.co））
- [原文](https://draven.co/autoreleasepool/) — 第三方博客（未归档（draven.co））
- [本地](blogs/zh/sunnyxx/%E9%BB%91%E5%B9%95%E8%83%8C%E5%90%8E%E7%9A%84autorelease-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) · [中文](blogs/zh/sunnyxx/%E9%BB%91%E5%B9%95%E8%83%8C%E5%90%8E%E7%9A%84autorelease-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) · [原文](https://blog.sunnyxx.com/2014/10/15/behind-autorelease/) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html) — 第三方博客
### Day 5｜把 ARC 拆成编译器与 runtime 两半（对应 W1-02）

- [原文](https://clang.llvm.org/docs/AutomaticReferenceCounting.html#semantics) — 第三方博客（未归档（clang.llvm.org））
- [本地](blogs/en/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html) — 第三方博客
- [本地](blogs/zh/sunnyxx/arc%E4%B8%8Bdealloc%E8%BF%87%E7%A8%8B%E5%8F%8A-cxx-destruct%E7%9A%84%E6%8E%A2%E7%A9%B6-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) · [中文](blogs/zh/sunnyxx/arc%E4%B8%8Bdealloc%E8%BF%87%E7%A8%8B%E5%8F%8A-cxx-destruct%E7%9A%84%E6%8E%A2%E7%A9%B6-sunnyxx%E7%9A%84%E6%8A%80%E6%9C%AF%E5%8D%9A%E5%AE%A2.md) · [原文](https://blog.sunnyxx.com/2014/04/02/objc_dig_arc_dealloc/) — 第三方博客

## 第二周：weak、属性关键字与 Block

### Day 1｜先把属性翻译成所有权关系（对应 W2-07、W2-08、W2-09）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/EncapsulatingData/EncapsulatingData.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/foundation/nscopying) — Apple 现行文档（未归档）
- [本地](blogs/en/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html) — 第三方博客
- [原文](https://www.objc.io/issues/7-foundation/value-objects/) — 第三方博客（未归档（objc.io））
- [原文](https://draven.co/rr/) — 第三方博客（未归档（draven.co））
- [本地](blogs/zh/yulingtianxia/objective-c-%E5%BC%95%E7%94%A8%E8%AE%A1%E6%95%B0%E5%8E%9F%E7%90%86.md) · [中文](blogs/zh/yulingtianxia/objective-c-%E5%BC%95%E7%94%A8%E8%AE%A1%E6%95%B0%E5%8E%9F%E7%90%86.md) · [原文](https://yulingtianxia.com/blog/2015/12/06/The-Principle-of-Refenrence-Counting/) — 第三方博客
- [原文](https://cloud.tencent.com/developer/article/2303898) — 第三方博客（未归档（cloud.tencent.com））
- [原文](https://github.com/pro648/tips/wiki/iOS%E4%B8%AD%E5%AE%9A%E4%B9%89%E5%B1%9E%E6%80%A7%E6%97%B6%E7%9A%84atomic%E3%80%81nonatomic%E3%80%81copy%E3%80%81assign%E3%80%81strong%E3%80%81weak%E7%AD%89%E5%87%A0%E4%B8%AA%E7%89%B9%E6%80%A7%E7%9A%84%E5%8C%BA%E5%88%AB) — GitHub 源码（待 clone 到 oss/）
### Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）

- [原文](https://clang.llvm.org/docs/AutomaticReferenceCounting.html) — 第三方博客（未归档（clang.llvm.org））
- [原文](https://github.com/apple-oss-distributions/objc4) — GitHub 源码（待 clone 到 oss/）
- [本地](blogs/en/mikeash/my-friday-q-a-post-this-week.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2010-07-16-zeroing-weak-references-in-objective-c.html) — 第三方博客
- [本地](blogs/en/alwaysprocessing/objective-c-internals-retain-objective-c-memory-is-managed-through-a-reference-counting-sc.md) · [原文](https://alwaysprocessing.blog/2023/07/22/objc-retain) — 第三方博客
- [原文](https://github.com/Desgard/iOS-Source-Probe/blob/master/Objective-C/Runtime/weak%20%E5%BC%B1%E5%BC%95%E7%94%A8%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F.md) — GitHub 源码（待 clone 到 oss/）
- [原文](https://blog.csdn.net/u013378438/article/details/82790332) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://www.uiimage.com/post/blog/ios/sidetables/) — 第三方博客（未归档（uiimage.com））
- [原文](https://draven.co/rr/) — 第三方博客（未归档（draven.co））
- [原文](https://verdagon.dev/blog/surprising-weak-refs) — 第三方博客（未归档（verdagon.dev））
- [本地](blogs/en/mikeash/friday-q-a-2017-09-22-swift-4-weak-references.md) · [原文](https://mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html) — 第三方博客
- [原文](https://github.com/apple-oss-distributions/objc4/blob/main/runtime/objc-weak.mm) — GitHub 源码（待 clone 到 oss/）
### Day 3｜先看 Block 是什么，再谈捕获（对应 W2-12、W2-13、W2-15）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://clang.llvm.org/docs/Block-ABI-Apple.html) — 第三方博客（未归档（clang.llvm.org））
- [本地](blogs/en/mikeash/friday-q-a-2008-12-26.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2008-12-26.html) — 第三方博客
- [原文](https://github.com/Desgard/iOS-Source-Probe/blob/master/Objective-C/Runtime/%E6%B5%85%E8%B0%88%20block%EF%BC%881%EF%BC%89%20-%20clang%20%E6%94%B9%E5%86%99%E5%90%8E%E7%9A%84%20block%20%E7%BB%93%E6%9E%84.md) — GitHub 源码（待 clone 到 oss/）
- [原文](https://www.jianshu.com/p/f0870fa95aac) — 第三方博客（未归档（jianshu.com））
- [原文](https://www.informit.com/articles/article.aspx?p=1749597&seqNum=12) — 第三方博客（未归档（informit.com））
### Day 4｜在结构体基础上研究捕获与复制（对应 W2-10、W2-11）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/bxVariables.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://clang.llvm.org/docs/Block-ABI-Apple.html) — 第三方博客（未归档（clang.llvm.org））
- [原文](https://github.com/Desgard/iOS-Source-Probe/blob/master/Objective-C/Runtime/%E6%B5%85%E8%B0%88%20block%EF%BC%882%EF%BC%89%20-%20%E6%88%AA%E8%8E%B7%E5%8F%98%E9%87%8F%E6%96%B9%E5%BC%8F.md) — GitHub 源码（待 clone 到 oss/）
- [原文](https://halfrost.com/ios_block/) — 第三方博客（未归档（halfrost.com））
### Day 5｜循环引用是 Day 4 所有权图的推论（对应 W2-14、W2-16）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/WorkingwithBlocks/WorkingwithBlocks.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://clang.llvm.org/docs/AutomaticReferenceCounting.html) — 第三方博客（未归档（clang.llvm.org））
- [原文](https://www.jianshu.com/p/809a9bca597f) — 第三方博客（未归档（jianshu.com））
- [本地](blogs/en/mikeash/friday-q-a-2011-09-30-automatic-reference-counting.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html) — 第三方博客
- [原文](https://luohs.github.io/2017/05/31/20170531/) — 第三方博客（未归档（luohs.github.io））
- [原文](https://github.com/draveness/analyze/blob/master/contents/FBRetainCycleDetector/iOS%20%E4%B8%AD%E7%9A%84%20block%20%E6%98%AF%E5%A6%82%E4%BD%95%E6%8C%81%E6%9C%89%E5%AF%B9%E8%B1%A1%E7%9A%84.md) — GitHub 源码（待 clone 到 oss/）
- [原文](https://lvv.me/posts/2022/08/13_weak_strong_dance/) — 第三方博客（未归档（lvv.me））
- [原文](https://dhoerl.wordpress.com/2013/04/23/i-finally-figured-out-weakself-and-strongself/) — 第三方博客（未归档（dhoerl.wordpress.com））
- [原文](https://bytes.vokal.io/objc-block-capture-weakself/) — 第三方博客（未归档（bytes.vokal.io））
- [原文](https://medium.com/fantageek/understanding-weak-and-strong-in-objective-c-d17ba4c2c297) — 第三方博客（未归档（medium.com））
### Day 6｜把 weak 与 Block 合成一张生命周期图

- [原文](https://github.com/apple-oss-distributions/objc4/blob/main/runtime/objc-weak.mm) — GitHub 源码（待 clone 到 oss/）
- [原文](https://clang.llvm.org/docs/Block-ABI-Apple.html) — 第三方博客（未归档（clang.llvm.org））

## 第三周：Runtime 行为与 Cocoa 对象通信

### Day 1｜把方法调用还原为“查找行为”（对应 W1-03）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtHowMessagingWorks.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/objectivec/objective-c_runtime) — Apple 现行文档（未归档）
- [本地](blogs/en/mikeash/friday-q-a-2009-03-13-intro-to-the-objective-c-runtime.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2017-06-30-dissecting-objc-msgsend-on-arm64.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2009-03-27-objective-c-message-forwarding.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html) — 第三方博客
- [原文](https://ridiculousfish.com/blog/posts/objc_msgsend.html) — 第三方博客（未归档（ridiculousfish.com））
- [原文](https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/) — 第三方博客（未归档（zhongwuzw.github.io））
- [原文](https://kingcos.me/posts/2019/objc_msgsend/) — 第三方博客（未归档（kingcos.me））
- [原文](https://github.com/apple-oss-distributions/objc4) — GitHub 源码（待 clone 到 oss/）
### Day 2｜有了方法查找，才学习 Swizzling（对应 W4-04）

- [原文](https://developer.apple.com/documentation/objectivec/objective-c_runtime) — Apple 现行文档（未归档）
- [原文](https://nshipster.com/method-swizzling/) — 第三方博客（未归档（nshipster.com））
- [原文](https://www.cnblogs.com/developer-ios/p/4948803.html) — 第三方博客（未归档（cnblogs.com））
### Day 3｜Category 是编译产物，关联对象是运行期旁路（对应 W4-05、W4-06）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjectiveC/Chapters/ocCategories.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [本地](blogs/en/alwaysprocessing/objective-c-internals-associated-references-a-comparison-of-apple-s-associated-references-.md) · [原文](https://alwaysprocessing.blog/2023/06/05/objc-assoc-obj) — 第三方博客
- [原文](https://draveness.me/ao.html) — 第三方博客（未归档（draveness.me））
- [原文](https://nshipster.com/associated-objects/) — 第三方博客（未归档（nshipster.com））
- [原文](https://www.cnblogs.com/huanying2000/p/13938350.html) — 第三方博客（未归档（cnblogs.com））
- [原文](https://github.com/apple-oss-distributions/objc4) — GitHub 源码（待 clone 到 oss/）
### Day 4｜用加载时机把 Category、load、initialize 串起来（对应 W5-07）

- [原文](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time) — Apple 现行文档（未归档）
- [原文](https://www.cnblogs.com/junhuawang/p/14304756.html) — 第三方博客（未归档（cnblogs.com））
### Day 5｜KVC 提供间接访问，KVO 在它的约定上插入通知（对应 W3-09）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOImplementation.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://nshipster.com/key-value-observing/) — 第三方博客（未归档（nshipster.com））
- [原文](https://www.neroxie.com/2019/07/12/KVC%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) — 第三方博客（未归档（neroxie.com））
- [原文](https://zhuanlan.zhihu.com/p/587704697) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [原文](https://blog.csdn.net/zhoupengju/article/details/53129436) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://huberyyang.com/2018/04/13/KVO%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/) — 第三方博客（未归档（huberyyang.com））
- [本地](blogs/en/mikeash/friday-q-a-2012-03-02-key-value-observing-done-right-take-2.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html) — 第三方博客
### Day 6｜最后才比较对象通信模式（对应 W3-01、W6-07）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/CocoaDesignPatterns/CocoaDesignPatterns.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/foundation/notificationcenter) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://www.objc.io/issues/7-foundation/communication-patterns/) — 第三方博客（未归档（objc.io））
- [原文](https://blog.csdn.net/weixin_38633659/article/details/149066468) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://www.cnblogs.com/iOS-Blog/archive/2013/02/21/2920926.html) — 第三方博客（未归档（cnblogs.com））
- [原文](https://coderjtao.github.io/2019/07/26/%E5%BA%95%E5%B1%82%E5%88%9D%E7%AA%A5%E2%80%94%E2%80%94NSNotificationCenter/) — 第三方博客（未归档（coderjtao.github.io））
- [原文](https://www.cnblogs.com/wujy/p/5825690.html) — 第三方博客（未归档（cnblogs.com））
- [原文](http://southpeak.github.io/2015/03/20/cocoa-foundation-nsnotificationcenter/) — 第三方博客（未归档（southpeak.github.io））

## 第四周：线程、GCD、Operation 与锁

### Day 1｜先看问题：共享可变状态（对应 W3-02）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/AboutThreads/AboutThreads.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://www.objc.io/issues/2-concurrency/low-level-concurrency-apis/) — 第三方博客（未归档（objc.io））
### Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/CreatingThreads/CreatingThreads.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html) — 第三方博客（未归档（pubs.opengroup.org））
- [原文](https://developer.apple.com/documentation/foundation/nsthread) — Apple 现行文档（未归档）
- [本地](blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) · [中文](blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) · [原文](https://blog.ibireme.com/2015/05/18/runloop/) — 第三方博客
- [原文](http://stevenwuzheng.com/archives/runloop%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB) — 第三方博客（未归档（stevenwuzheng.com））
- [原文](https://bujige.net/blog/iOS-Complete-learning-pthread-and-NSThread.html) — 第三方博客（未归档（bujige.net））
- [本地](blogs/en/mikeash/friday-q-a-2016-04-15-performance-comparisons-of-common-operations-2016-edition.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2016-04-15-performance-comparisons-of-common-operations-2016-edition.html) — 第三方博客
### Day 3｜GCD 从四格矩阵开始，再扩 API（对应 W3-06）

- [原文](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/OperationQueues/OperationQueues.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/dispatch/dispatchqueue) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/barrier) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/dispatch/dispatchsource) — Apple 现行文档（未归档）
- [原文](https://www.objc.io/issues/2-concurrency/common-background-practices/) — 第三方博客（未归档（objc.io））
- [本地](blogs/en/mikeash/friday-q-a-2015-09-04-let-s-build-dispatch-queue.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2015-09-04-lets-build-dispatch_queue.html) — 第三方博客
- [本地](blogs/en/mikeash/friday-q-a-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html) — 第三方博客
- [原文](https://blog.devtang.com/2012/02/22/use-gcd/) — 第三方博客（未归档（blog.devtang.com））
- [原文](https://ming1016.github.io/2016/01/13/how-to-use-gcd/) — 第三方博客（未归档（ming1016.github.io））
- [原文](https://www.cnblogs.com/bbqzsl/p/5287970.html) — 第三方博客（未归档（cnblogs.com））
- [原文](https://dirtmelon.github.io/Knowledge/iDev/Multithreading/Grand-Central-Dispatch.html) — 第三方博客（未归档（dirtmelon.github.io））
### Day 4｜Operation 是“可管理的任务图”（对应 W3-05）

- [原文](https://developer.apple.com/documentation/foundation/operation) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/foundation/operationqueue) — Apple 现行文档（未归档）
- [原文](https://nshipster.com/nsoperation/) — 第三方博客（未归档（nshipster.com））
- [原文](https://nsprogrammer.github.io/jekyll/update/2021/07/02/nsoperation.html) — 第三方博客（未归档（nsprogrammer.github.io））
- [原文](https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios) — 第三方博客（未归档（shakuro.com））
- [原文](https://ioscoachfrank.com/chaining-nsoperations.html) — 第三方博客（未归档（ioscoachfrank.com））
### Day 5｜队列不是线程，QoS 不是绝对优先级（对应 W3-07、W3-08）

- [原文](https://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/dispatch/dispatchqos) — Apple 现行文档（未归档）
- [原文](https://www.objc.io/issues/2-concurrency/concurrency-apis-and-pitfalls/) — 第三方博客（未归档（objc.io））
### Day 6｜锁的学习方式是“按约束选择”（对应 W3-11）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/ThreadSafety/ThreadSafety.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/os/os_unfair_lock) — Apple 现行文档（未归档）
- [原文](https://www.objc.io/issues/2-concurrency/thread-safe-class-design/) — 第三方博客（未归档（objc.io））
- [本地](blogs/en/mikeash/friday-q-a-2017-10-27-locks-thread-safety-and-swift-2017-edition.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html) — 第三方博客
- [原文](https://mjtsai.com/blog/2015/12/16/osspinlock-is-unsafe/) — 第三方博客（未归档（mjtsai.com））
- [原文](https://zhuanlan.zhihu.com/p/587418305) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [原文](https://juejin.cn/post/7070416276564213791) — 第三方博客（未归档（juejin.cn））
- [原文](https://solarana.dev/2018/04/15/protecting-critical-sections/) — 第三方博客（未归档（solarana.dev））

## 第五周：RunLoop、AutoreleasePool、响应者链与生命周期

### Day 1｜RunLoop 先学“一轮发生什么”（对应 W4-02）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/documentation/corefoundation/cfrunloop) — Apple 现行文档（未归档）
- [原文](https://suelan.github.io/2021/02/13/20210213-dive-into-runloop-ios/) — 第三方博客（未归档（suelan.github.io））
- [原文](https://meldstudio.co/blog/macos-cfrunloop-internals-scheduling-high-precision-timers-and-recurring-tasks/) — 第三方博客（未归档（meldstudio.co））
- [原文](https://www.jianshu.com/p/aa0fae8c491b) — 第三方博客（未归档（jianshu.com））
- [原文](https://www.desgard.com/iOS-Source-Probe/Objective-C/Foundation/Run%20Loop%20%E8%AE%B0%E5%BD%95%E4%B8%8E%E6%BA%90%E7%A0%81%E6%B3%A8%E9%87%8A.html) — 第三方博客（未归档（desgard.com））
### Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）

- [本地](blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) · [中文](blogs/zh/ibireme/%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3runloop.md) · [原文](https://blog.ibireme.com/2015/05/18/runloop/) — 第三方博客
- [原文](https://github.com/Tencent/matrix/wiki) — GitHub 源码（待 clone 到 oss/）
- [原文](https://cloud.tencent.cn/developer/article/1427933) — 第三方博客（未归档（cloud.tencent.cn））
- [原文](https://www.jessesquires.com/blog/2022/08/11/implementing-a-main-thread-watchdog-on-ios/) — 第三方博客（未归档（jessesquires.com））
- [原文](https://engineering.fb.com/2015/06/25/ios/delivering-high-scroll-performance/) — 第三方博客（未归档（engineering.fb.com））
- [原文](https://ai-chan.top/code/Runloop%E4%B8%8E%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7/) — 第三方博客（未归档（ai-chan.top））
- [原文](https://cloud.tencent.com/developer/article/1895911) — 第三方博客（未归档（cloud.tencent.com））
- [原文](https://github.com/didi/DoKit) — GitHub 源码（待 clone 到 oss/）
### Day 3｜AutoreleasePool 放回事件循环中理解（对应 W4-01）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAutoreleasePools.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://github.com/apple-oss-distributions/objc4) — GitHub 源码（待 clone 到 oss/）
- [本地](blogs/en/mikeash/friday-q-a-2011-09-02-let-s-build-nsautoreleasepool.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html) — 第三方博客
- [原文](https://blog.csdn.net/Deft_MKJing/article/details/82947706) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://jinxuebin.cn/2019/06/AutoReleasePool%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86%E6%8E%A2%E7%A9%B6/) — 第三方博客（未归档（jinxuebin.cn））
- [原文](https://devyang.space/2019/05/05/autoreleasepool/) — 第三方博客（未归档（devyang.space））
- [原文](http://matteogobbi.github.io/blog/2014/09/28/autorelease-under-the-hood/) — 第三方博客（未归档（matteogobbi.github.io））
### Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）

- [本地](apple-docs/en/uikit/using-responders-and-the-responder-chain-to-handle-events.md) · [原文](https://developer.apple.com/documentation/uikit/using-responders-and-the-responder-chain-to-handle-events) — Apple 现行文档
- [原文](https://developer.apple.com/documentation/uikit/uiresponder) — Apple 现行文档（未归档）
- [原文](https://swiftrocks.com/understanding-the-ios-responder-chain) — 第三方博客（未归档（swiftrocks.com））
- [原文](https://medium.com/ios-os-x-development/understanding-cocoa-and-cocoa-touch-responder-chain-12fe558ebe97) — 第三方博客（未归档（medium.com））
- [原文](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/) — 第三方博客（未归档（cocoanetics.com））
- [原文](https://bbs.huaweicloud.com/blogs/331365) — 第三方博客（未归档（bbs.huaweicloud.com））
### Day 5｜生命周期必须按场景观测（对应 W5-06）

- [原文](https://developer.apple.com/documentation/uikit/uiviewcontroller) — Apple 现行文档（未归档）
- [原文](https://medium.com/@dhrumilraval212/mastering-the-uiviewcontroller-lifecycle-a-senior-developers-deep-dive-4cc8082cd3d6) — 第三方博客（未归档（medium.com））
- [原文](https://useyourloaf.com/blog/uikit-view-lifecycle-viewisappearing/) — 第三方博客（未归档（useyourloaf.com））
- [原文](https://www.jessesquires.com/blog/2023/02/20/ios-view-controller-loading/) — 第三方博客（未归档（jessesquires.com））
### Day 6｜最后补坐标系，因为它依赖视图层级（对应 W3-12、W5-08）

- [原文](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/WindowsandViews/WindowsandViews.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://www.objc.io/issues/12-animations/animations-explained/) — 第三方博客（未归档（objc.io））
- [原文](https://joeshang.github.io/2014-12-19-understand-anchorpoint-position-frame/) — 第三方博客（未归档（joeshang.github.io））
- [原文](https://zhangbuhuai.com/post/layer-geometry-in-ios.html) — 第三方博客（未归档（zhangbuhuai.com））
- [原文](http://www.samirchen.com/graphic-transform-in-ios/) — 第三方博客（未归档（samirchen.com））
- [原文](https://www.jianshu.com/p/e1fec2f92c63) — 第三方博客（未归档（jianshu.com））

## 第六周：UIKit 渲染、UITableView 与性能

### Day 1｜先弄清“谁保存状态，谁把像素送上屏”（对应 W5-04）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/index.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/CoreAnimationBasics/CoreAnimationBasics.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
### Day 2｜离屏渲染先学定义，再看触发条件（对应 W5-02）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/SettingUpLayerObjects/SettingUpLayerObjects.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://www.objc.io/issue-3/moving-pixels-onto-the-screen.html) — 第三方博客（未归档（objc.io））
- [原文](https://www.hackingwithswift.com/articles/155/advanced-uiview-shadow-effects-using-shadowpath) — 第三方博客（未归档（hackingwithswift.com））
- [原文](http://angelolloqui.com/blog/30-iOS-Performance-tips-I-Drawing-shadows) — 第三方博客（未归档（angelolloqui.com））
- [原文](https://github.com/seedante/OptimizationForOffscreenRender) — GitHub 源码（待 clone 到 oss/）
- [原文](https://blog.fearcat.in/a?ID=01750-5926f776-644b-465e-8d4d-d6c7b854e533) — 第三方博客（未归档（blog.fearcat.in））
- [原文](https://www.jianshu.com/p/e6d44ca9c103) — 第三方博客（未归档（jianshu.com））
### Day 3｜UITableView 先从协议契约学，不先背调用顺序（对应 W5-03、W5-05）

- [本地](apple-docs/en/uikit/filling-a-table-with-data.md) · [原文](https://developer.apple.com/documentation/uikit/filling-a-table-with-data) — Apple 现行文档
- [原文](https://developer.apple.com/documentation/uikit/uitableviewdatasource) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/uikit/uitableviewdelegate) — Apple 现行文档（未归档）
- [原文](https://www.objc.io/issues/1-view-controllers/table-views/) — 第三方博客（未归档（objc.io））
### Day 4｜先建立 baseline，再谈列表优化（对应 W6-09）

- [原文](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/xcode/performance-and-metrics) — Apple 现行文档（未归档）
- [本地](apple-docs/en/uikit/filling-a-table-with-data.md) · [原文](https://developer.apple.com/documentation/uikit/filling-a-table-with-data) — Apple 现行文档
- [原文](https://medium.com/jike-engineering/asyncdisplaykit%E4%BB%8B%E7%BB%8D-%E4%B8%80-6b871d29e005) — 第三方博客（未归档（medium.com））
- [原文](https://www.swiftcafe.io/post/asdk) — 第三方博客（未归档（swiftcafe.io））
- [原文](https://medium.com/@iosengineering/better-uitableviews-pt-1-performance-a76dcd76d772) — 第三方博客（未归档（medium.com））
- [原文](https://blog.aberlt.com/2017/12/30/UITableView-%E6%B5%81%E7%95%85%E5%BA%A6%E4%BC%98%E5%8C%96%E5%AE%9E%E8%B7%B5/) — 第三方博客（未归档（blog.aberlt.com））
### Day 5｜集合先学稳定语义，再看某版本实现（对应 W6-10）

- [原文](https://developer.apple.com/documentation/foundation/nsdictionary) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/foundation/nsmutablearray) — Apple 现行文档（未归档）
- [原文](https://github.com/apple-oss-distributions/CF) — GitHub 源码（待 clone 到 oss/）
- [原文](https://ciechanow.ski/exposing-nsmutablearray/) — 第三方博客（未归档（ciechanow.ski））
- [原文](https://ciechanow.ski/exposing-nsdictionary/) — 第三方博客（未归档（ciechanow.ski））
- [原文](http://blog.joyingx.me/2015/05/03/NSMutableArray%20%E5%8E%9F%E7%90%86%E6%8F%AD%E9%9C%B2/) — 第三方博客（未归档（blog.joyingx.me））
- [原文](https://zhuanlan.zhihu.com/p/25063245) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [原文](https://www.laoqingcai.com/ios-nsmutablearray/) — 第三方博客（未归档（laoqingcai.com））
### Day 6｜完成一次真正的性能闭环（对应 W5-02～W5-05、W6-09、W6-10）

- [原文](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/xcode/performance-and-metrics) — Apple 现行文档（未归档）

## 第七周：编译、链接、Mach-O、dyld 与 App 启动

### Day 1｜从一份源文件走到目标文件（对应 W1-07）

- [本地](wwdc/en/wwdc2018/415-behind-the-scenes-of-the-xcode-build-process.md) · [原文](https://developer.apple.com/videos/play/wwdc2018/415/) — WWDC
- [本地](blogs/en/mikeash/friday-q-a-2009-11-06-linking-and-install-names.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2009-11-06-linking-and-install-names.html) — 第三方博客
- [原文](https://segmentfault.com/a/1190000047731614) — 第三方博客（未归档（segmentfault.com））
### Day 2｜目标文件有了，才学习 Mach-O（对应 W1-07 展开）

- [原文](https://developer.apple.com/documentation/kernel/mach-o) — Apple 现行文档（未归档）
- [本地](blogs/en/mikeash/friday-q-a-2012-11-30-let-s-build-a-mach-o-executable.md) · [原文](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html) — 第三方博客
### Day 3｜静态/动态不是文件后缀问答（对应 W1-09）

- [原文](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/000-Introduction/Introduction.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/forums/thread/715385) — Apple 其它
- [原文](https://pewpewthespells.com/blog/static_and_dynamic_libraries.html) — 第三方博客（未归档（pewpewthespells.com））
- [原文](https://bpoplauschi.github.io/2021/10/24/Intro-to-static-and-dynamic-libraries-frameworks.html) — 第三方博客（未归档（bpoplauschi.github.io））
- [原文](https://engineering.monday.com/is-there-such-a-thing-as-a-static-framework/) — 第三方博客（未归档（engineering.monday.com））
### Day 4｜在 Mach-O 基础上学习 dyld（对应 W1-08）

- [本地](wwdc/en/wwdc2022/110362-link-fast-improve-build-and-launch-times.md) · [原文](https://developer.apple.com/videos/play/wwdc2022/110362/) — WWDC
- [原文](https://github.com/apple-oss-distributions/dyld) — GitHub 源码（待 clone 到 oss/）
- [原文](https://ddeville.me/2014/04/dynamic-linking/) — 第三方博客（未归档（ddeville.me））
- [原文](https://blog.allegro.tech/2018/05/Static-linking-vs-dyld3.html) — 第三方博客（未归档（blog.allegro.tech））
- [原文](https://huang-libo.github.io/posts/App-Startup-Time-dyld/) — 第三方博客（未归档（huang-libo.github.io））
- [原文](https://zhuanlan.zhihu.com/p/597864788) — 第三方博客（未归档（zhuanlan.zhihu.com））
- [原文](https://blog.jacobstechtavern.com/p/static-dynamic-mergeable-oh-my) — 第三方博客（未归档（blog.jacobstechtavern.com））
### Day 5｜把 Runtime 初始化放进 App 冷启动（对应 W6-08）

- [原文](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time) — Apple 现行文档（未归档）
- [本地](wwdc/en/wwdc2019/423-optimizing-app-launch.md) · [原文](https://developer.apple.com/videos/play/wwdc2019/423/) — WWDC
- [原文](https://developer.apple.com/documentation/xcode/performance-and-metrics) — Apple 现行文档（未归档）
- [原文](https://www.avanderlee.com/optimization/launch-time-performance-optimization/) — 第三方博客（未归档（avanderlee.com））
- [原文](https://tech.meituan.com/2018/12/06/waimai-ios-optimizing-startup.html) — 第三方博客（未归档（tech.meituan.com））
- [原文](https://mp.weixin.qq.com/s/Drmmx5JtjG3UtTFksL6Q8Q) — 第三方博客（未归档（mp.weixin.qq.com））
- [原文](https://www.emergetools.com/blog/posts/iOS15LaunchTime) — 第三方博客（未归档（emergetools.com））
- [原文](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles) — 第三方博客（未归档（emergetools.com））
- [原文](https://engineering.fb.com/2023/02/06/ios/facebook-ios-app-architecture/) — 第三方博客（未归档（engineering.fb.com））
### Day 6｜启动优化也必须是测量闭环（对应 W1-07～W1-09、W6-08）

- [原文](https://developer.apple.com/documentation/xcode/reducing-your-app-s-launch-time) — Apple 现行文档（未归档）
- [本地](wwdc/en/wwdc2019/423-optimizing-app-launch.md) · [原文](https://developer.apple.com/videos/play/wwdc2019/423/) — WWDC

## 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）

### Day 1｜先做存储选择，不先钻数据库实现（对应 W3-10）

- [原文](https://developer.apple.com/documentation/foundation/using-the-file-system-effectively) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/foundation/userdefaults) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/security/keychain-services) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/coredata/) — Apple 现行文档（未归档）
- [原文](https://www.objc.io/issues/4-core-data/core-data-overview/) — 第三方博客（未归档（objc.io））
### Day 2｜有了存储场景，再补数据库最低原理（对应 W6-15、W6-16）

- [原文](https://www.sqlite.org/lang.html) — 第三方博客（未归档（sqlite.org））
- [原文](https://www.sqlite.org/lang_transaction.html) — 第三方博客（未归档（sqlite.org））
- [原文](https://www.sqlite.org/fileformat2.html) — 第三方博客（未归档（sqlite.org））
- [原文](https://xiaolincoding.com/interview/mysql.html) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://xiaolincoding.com/mysql/index/why_index_chose_bpuls_tree.html) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://xiaolincoding.com/mysql/index/page.html) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://github.com/halfrost/Halfrost-Field/blob/master/contents/iOS/Realm/Realm%E6%95%B0%E6%8D%AE%E5%BA%93%20%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E2%80%9C%E6%94%BE%E5%BC%83%E2%80%9D.md) — GitHub 源码（待 clone 到 oss/）
- [原文](https://www.bswanson.dev/blog/exploring-sqlite-internals/) — 第三方博客（未归档（bswanson.dev））
- [原文](https://www.cnblogs.com/huahuahu/p/sqlite-suo-yin-de-yuan-li-ji-ying-yong.html) — 第三方博客（未归档（cnblogs.com））
### Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09）

- [原文](https://www.rfc-editor.org/rfc/rfc8259) — 第三方博客（未归档（rfc-editor.org））
- [原文](https://www.w3.org/TR/xml/) — 第三方博客（未归档（w3.org））
- [原文](https://protobuf.dev/programming-guides/encoding/) — 第三方博客（未归档（protobuf.dev））
- [原文](https://protobuf.dev/programming-guides/json/) — 第三方博客（未归档（protobuf.dev））
- [原文](https://developer.apple.com/documentation/foundation/jsonserialization) — Apple 现行文档（未归档）
- [原文](https://kreya.app/blog/protocolbuffers-wire-format/) — 第三方博客（未归档（kreya.app））
- [原文](https://kreya.app/blog/protocolbuffers-wire-format-part-2/) — 第三方博客（未归档（kreya.app））
- [原文](https://victoriametrics.com/blog/go-protobuf/) — 第三方博客（未归档（victoriametrics.com））
- [原文](https://auth0.com/blog/beating-json-performance-with-protobuf/) — 第三方博客（未归档（auth0.com））
### Day 4｜JSONModel 只追一条主链（对应 W6-03）

- [原文](https://github.com/jsonmodel/jsonmodel) — GitHub 源码（待 clone 到 oss/）
- [原文](https://developer.apple.com/documentation/objectivec/objective-c_runtime) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://knightsj.github.io/2017/02/22/JSONModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90/) — 第三方博客（未归档（knightsj.github.io））
### Day 5｜用同一组问题读 YYModel，才有可比性（对应 W6-04）

- [原文](https://github.com/ibireme/YYModel) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/ibireme/YYModel/blob/master/YYModel/NSObject%2BYYModel.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/ibireme/YYModel/blob/master/YYModel/YYClassInfo.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://blog.csdn.net/game3108/article/details/52388089) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://blog.csdn.net/Lu_Ca/article/details/114532423) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://blog.itlee.top/2017/12/21/YYModel%E6%BA%90%E7%A0%81%E8%A7%A3%E6%9E%90%E4%B8%80/) — 第三方博客（未归档（blog.itlee.top））
### Day 6｜SDWebImage 第一遍只看成功路径（对应 W6-05）

- [原文](https://sdwebimage.github.io/) — 第三方博客（未归档（sdwebimage.github.io））
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/UIImageView%2BWebCache.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDWebImageManager.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDImageCache.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDWebImageDownloader.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://developer.apple.com/documentation/foundation/url-loading-system) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/documentation/foundation/urlcache) — Apple 现行文档（未归档）
- [原文](http://southpeak.github.io/2015/02/07/sourcecode-sdwebimage/) — 第三方博客（未归档（southpeak.github.io））
- [原文](https://www.cnblogs.com/zhangzhang-y/p/13584570.html) — 第三方博客（未归档（cnblogs.com））
### Day 7｜第二遍才看性能与取消（对应 W6-05、W6-09）

- [原文](https://github.com/SDWebImage/SDWebImage) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage/wiki/5.6-Code-Architecture-Analysis) — GitHub 源码（待 clone 到 oss/）
- [原文](https://looseyi.github.io/post/sourcecode-ios/source-code-sdweb-en1/) — 第三方博客（未归档（looseyi.github.io））
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDWebImageManager.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDWebImageDownloader.m) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage/blob/master/SDWebImage/Core/SDImageCache.m) — GitHub 源码（待 clone 到 oss/）
### Day 8｜架构是前七天代码的职责重排（对应 W6-06、W6-07）

- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/CocoaDesignPatterns/CocoaDesignPatterns.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Model-View-Controller/Model-View-Controller.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://www.objc.io/issues/13-architecture/mvvm/) — 第三方博客（未归档（objc.io））
- [原文](https://www.objc.io/issues/13-architecture/) — 第三方博客（未归档（objc.io））
- [原文](https://www.objc.io/books/app-architecture/) — 第三方博客（未归档（objc.io））
- [原文](https://blog.csdn.net/weixin_46818265/article/details/142442895) — 第三方博客（未归档（blog.csdn.net））
- [原文](https://www.jianshu.com/p/e59bb8f59302) — 第三方博客（未归档（jianshu.com））
### Day 9｜网络基础放到 URLSession 下面分层（对应 W6-02、W6-11、W6-12）

- [原文](https://developer.apple.com/documentation/foundation/url-loading-system) — Apple 现行文档（未归档）
- [原文](https://www.rfc-editor.org/rfc/rfc9110) — 第三方博客（未归档（rfc-editor.org））
- [原文](https://www.rfc-editor.org/rfc/rfc9293) — 第三方博客（未归档（rfc-editor.org））
- [原文](https://www.rfc-editor.org/rfc/rfc8200) — 第三方博客（未归档（rfc-editor.org））
- [原文](https://www.xiaolincoding.com/network/) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://www.xiaolincoding.com/network/2_http/http_interview.html) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://javaguide.cn/cs-basics/network/tcp-connection-and-disconnection.html) — 第三方博客（未归档（javaguide.cn））
- [原文](https://segmentfault.com/a/1190000022410446) — 第三方博客（未归档（segmentfault.com））
- [原文](https://www.xiaolincoding.com/network/2_http/http3.html) — 第三方博客（未归档（xiaolincoding.com））
### Day 10｜用一个小项目证明知识连接起来了（对应 全阶段串联）

- [原文](https://developer.apple.com/documentation/foundation/urlsession) — Apple 现行文档（未归档）
- [原文](https://github.com/jsonmodel/jsonmodel) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/ibireme/YYModel) — GitHub 源码（待 clone 到 oss/）
- [原文](https://github.com/SDWebImage/SDWebImage) — GitHub 源码（待 clone 到 oss/）
- [原文](https://developer.apple.com/documentation/uikit/uitableview) — Apple 现行文档（未归档）
- [原文](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html) — Apple 旧归档（在旧仓库 apple-developer-archive-vault）
- [原文](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html) — 第三方博客（未归档（pubs.opengroup.org））
- [原文](https://www.rfc-editor.org/rfc/rfc9110) — 第三方博客（未归档（rfc-editor.org））
- [原文](https://www.rfc-editor.org/rfc/rfc9293) — 第三方博客（未归档（rfc-editor.org））
- [原文](https://www.xiaolincoding.com/os/) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://www.xiaolincoding.com/network/) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://www.sqlite.org/lang.html) — 第三方博客（未归档（sqlite.org））
- [原文](https://www.sqlite.org/lang_transaction.html) — 第三方博客（未归档（sqlite.org））
- [原文](https://www.sqlite.org/fileformat2.html) — 第三方博客（未归档（sqlite.org））
- [原文](https://xiaolincoding.com/interview/mysql.html) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://xiaolincoding.com/mysql/index/page.html) — 第三方博客（未归档（xiaolincoding.com））
- [原文](https://leetcode.cn/studyplan/top-100-liked/) — 第三方博客（未归档（leetcode.cn））
- [原文](https://leetcode.cn/problems/lru-cache/) — 第三方博客（未归档（leetcode.cn））
- [原文](https://leetcode.cn/problems/top-k-frequent-elements/) — 第三方博客（未归档（leetcode.cn））
- [原文](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/video_galleries/lecture-videos/) — 第三方博客（未归档（ocw.mit.edu））
- [原文](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/6d1ae5278d02bbecb5c4428928b24194_MIT6_006S20_lec3.pdf) — 第三方博客（未归档（ocw.mit.edu））
- [原文](https://opendatastructures.org/) — 第三方博客（未归档（opendatastructures.org））
- [原文](https://www.jianshu.com/p/809a9bca597f) — 第三方博客（未归档（jianshu.com））
- [原文](https://baijiahao.baidu.com/s?id=1670083688956388773&wfr=spider&for=pc) — 第三方博客（未归档（baijiahao.baidu.com））
