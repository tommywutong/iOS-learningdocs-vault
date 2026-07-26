---
title: FBAllocationTracker
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/fballocationtracker/'
original_language: zh
published: 2021-11-02
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:7d3fcf683c93283c'
translated: n/a
---

> 原文：[FBAllocationTracker](https://dirtmelon.github.io/posts/fballocationtracker/)　·　dirtmelon

## 简单介绍下

[FBAllocationTracker](https://github.com/facebookarchive/FBAllocationTracker) 是 Facebook 开源的一个用于查找当前存活的 Objective-C 对象的工具库。 FBAllocationTracker 提供了查找在内存中的 Objective-C 对象的接口。它可以获取指定类的所有对象，也可以像 Instruments 那样进行内存增长标记，然后只查找标记时间内创建的对象。 FBAllocationTracker 支持两种模式：记录对象和只是计算 `alloc/dealloc` 。第一种模式需要的操作步骤更多点，然后如果只是想进行统计，不想影响性能，可以使用第二种模式。相关操作接口由 `FBAllocationTrackerManager` 提供：

```objc
#import <FBAllocationTracker/FBAllocationTrackerManager.h>

int main(int argc, char * argv[]) {
  [[FBAllocationTrackerManager sharedManager] startTrackingAllocations];
  [[FBAllocationTrackerManager sharedManager] enableGenerations];
  @autoreleasepool {
      return UIApplicationMain(argc, argv, nil, NSStringFromClass([AppDelegate class]));
  }
}
```

`startTrackingAllocations` 方法会 swizzle `NSObject` 的 `+alloc` 和 `-dealloc` 方法，以此来计算对象的初始化和释放，而 `enableGenerations` 则会开始跟踪对象实例。

```objc
NSArray<FBAllocationTrackerSummary *> *summaries = [[FBAllocationTrackerManager sharedManager] currentAllocationSummary];
```

`FBAllocationTrackerSummary` 会记录类对应的对象个数，也可以获取特定类的对象：

```objc
NSArray *instances =[[FBAllocationTrackerManager sharedManager] instancesOfClasses:@[[ViewController class]]];
```

Generations 的操作则类似于 Instruments 的 Allocations ，可以通过 `markGeneration` 来区分不同时间段内创建的对象：

```objc
- (void)someFunction {
  // Enable generations (if not already enabled in main.m)
  [[FBAllocationTrackerManager sharedManager] enableGenerations];

  // Object a will be kept in generation with index 0
  NSObject *a = [NSObject new];

  // We are marking new generation
  [[FBAllocationTrackerManager sharedManager] markGeneration];

  // Objects b and c will be kept in second generation at index 1
  NSObject *b = [NSObject new];
  NSObject *c = [NSObject new];

  [[FBAllocationTrackerManager sharedManager] markGeneration];

  // Object d will be kept in third generation at index 2
  NSObject *d = [NSObject new];
}
```

## 开启计数记录

`FBAllocationTrackerManager` 的 `startTrackingAllocations` 实现比较简单，只是调用了一下 `AllocationTracker` 的 `beginTracking` 方法：

```objc
- (void)startTrackingAllocations
{
  FB::AllocationTracker::beginTracking();
}
```

`FB:: AllocationTracker:: beginTracking` 则调用了 `turnOnTracking` 方法来进行 swizzle ：

```objc
void beginTracking() {
  std::lock_guard<std::mutex> l(*_lock);

  if (_trackingInProgress) {
    return;
  }

  _trackingInProgress = true;

  turnOnTracking();
}
```

`lock_guard` 是基于 `mutex` 进行封装的，提供了 RAII 风格的机制，会在作用域内拥有一个 `mutex` 的变量。当创建一个 `lock_guard` 对象时，它会去获取 `mutex` 的所有权，当函数执行完毕，离开 `lock_guard` 所在的作用域时， `lock_guard` 会进行析构，而 `mutex` 也会被释放掉。

`turnOnTracking` 则负责对 `alloc` 和 `dealloc` 方法进行 swizzle ，常规的 swizzle 操作，这里就不展开说明了：

```objc
void turnOnTracking(void) {
  prepareOriginalMethods();

  replaceSelectorWithSelector([NSObject class],
                              @selector(allocWithZone:),
                              @selector(fb_newAllocWithZone:),
                              FBClassMethod);

  replaceSelectorWithSelector([NSObject class],
                              sel_registerName("dealloc"),
                              @selector(fb_newDealloc),
                              FBInstanceMethod);
}
```

FBAllocationTracker 会在 `alloc` 方法中对创建的对象进行记录：

```objc
+ (id)fb_newAllocWithZone:(id)zone
{
  id object = [self fb_originalAllocWithZone:zone];
  FB::AllocationTracker::incrementAllocations(object);
  return object;
}

void incrementAllocations(__unsafe_unretained id obj) {
  Class aCls = [obj class];

  // 1. _shouldTrackClass 的实现非常简单，只是做了下防空判断，以及如果是 NSTaggedPointerStringCStringContainer 则跳过记录
  if (!_shouldTrackClass(aCls)) {
    return;
  }
  // 2. 常规的 lock_guard 操作
  std::lock_guard<std::mutex> l(*_lock);

  // 3. 使用 _allocations 记录计数
  if (_trackingInProgress) {
    (*_allocations)[aCls]++;
  }

  // 4. 使用 _generationManager 记录对象
  if (_generationManager) {
    _generationManager->addObject(obj);
  }
}
```

`incrementAllocations` 的实现也比较简单，都是调用相关 API 。 `TrackerMap` 定义如下：

```objc
using TrackerMap =
  std::unordered_map<
  __unsafe_unretained Class,
  NSUInteger,
  FB::AllocationTracker::ClassHashFunctor,
  FB::AllocationTracker::ClassEqualFunctor>
```

`Class` 为 `key` ， 相关计数为 `value` ， `ClassHashFunctor` 和 `ClassEqualFunctor` 的实现：

```objc
struct ClassHashFunctor {
  size_t operator()(const Class key) const {
    // 使用 size_t 对 Class 进行转换
    return (size_t)(key);
  }
};

struct ClassEqualFunctor {
  bool operator()(const Class left, const Class right) const {
    return left == right;
  }
};
```

`incrementDeallocations` 的实现也和 `incrementAllocations` 类似，只不过使用了另外一个 `map` 来进行 `dealloc` 的计数：

```objc
void incrementDeallocations(__unsafe_unretained id obj) {
  Class aCls = [obj class];

  if (!_shouldTrackClass(aCls)) {
    return;
  }

  std::lock_guard<std::mutex> l(*_lock);

  // _deallocations 也是相同的 unordered_map
  if (_trackingInProgress) {
    (*_deallocations)[aCls]++;
  }

  if (_generationManager) {
    _generationManager->removeObject(obj);
  }
}
```

计数相关操作就介绍完毕了，操作也比较简单：

1. 记录

  的

  调用次数；
2. 记录

  的

  调用次数。

## 跟踪对象实例

上面的计数操作只是对次数进行记录，记录的维度是 `Class` 级别，没有记录每个对象，如果想要对对象也进行记录，就需要调用 Generation 的相关方法。

开启跟踪对象：

```objc
/// FBAllocationTrackerManager
- (void)enableGenerations
{
  dispatch_sync(_queue, ^{
    if (self->_generationsClients == 0) {
      FB::AllocationTracker::enableGenerations();
      FB::AllocationTracker::markGeneration();
    }
    self->_generationsClients += 1;
  });
}

/// AllocationTracker
void enableGenerations() {
  std::lock_guard<std::mutex> l(*_lock);

  if (_generationManager) {
    return;
  }
  /// 创建 `GenerationManager` ，`GenerationManager` 负责维护对象和 `Generation` 之间的映射关系。
  _generationManager = new GenerationManager();
}

/// AllocationTracker
void markGeneration(void) {
  std::lock_guard<std::mutex> l(*_lock);
  if (_generationManager) {
    _generationManager->markGeneration();
  }
}
```

### Generation 与 GenerationManager

`Generation` 则实现了类似 Instruments 的 `allocations` 操作，让你对特定时间段内创建的对象进行标记。 `Generation` 提供了一个以 `Class` 为 `key` ， `value` 为 `unordered_set<__unsafe_unretained id>` ，也就是说可以根据 `Class` 或者指定 `Generation` 来查找所包含的对象。`Generation` 的属性也比较简单，只有一个 `objects` 属性：

```cpp
typedef std::unordered_set<__unsafe_unretained id, ObjectHashFunctor, ObjectEqualFunctor> GenerationList;

typedef std::unordered_map<Class, GenerationList, ClassHashFunctor, ClassEqualFunctor> GenerationMap;
class Generation {
  private:
    GenerationMap objects;
  };
}
```

`GenerationMap` 对外也提供了相关的添加和移除操作：

```cpp
void Generation::add(__unsafe_unretained id object) {
  Class aCls = [object class];
  objects[aCls].insert(object);
}

  void Generation::remove(__unsafe_unretained id object) {
    Class aCls = [object class];
    objects[aCls].erase(object);
  }
```

`GenerationManager` 负责管理 `Generation` ，它提供了在 O(1) 时间复杂度内查找指针来自哪个 `Generation` 的操作。包含两个私有属性：

```cpp
// 用于在 O(1) 时间内查找对象来自哪一个 Generation ，提高性能
std::unordered_map<__unsafe_unretained id, NSInteger, ObjectHashFunctor, ObjectEqualFunctor> generationMapping;
// Generation 对应的 vector
std::vector<Generation> generations;
```

调用 `markGeneration` 方法可以创建新的 `Generation` ，添加到 `generations` 中，而 `GenerationManager` 会把创建的对象加到最新的 `Generation` 中：

```cpp
void GenerationManager::markGeneration() {
  generations.emplace_back(Generation {});
}
```

`addObject` 方法则会把 `object` 添加到 `lastGeneration` 中，同时建立 `object` 和 `Generation` 的映射关系：

```cpp
void GenerationManager::addObject(__unsafe_unretained id object){
  NSInteger numberOfGenerations = generations.size();
  if (numberOfGenerations == 0) {
    return;
  }

  Generation &lastGeneration = generations.back();
  // 所对应的层级为当前的 size - 1
  generationMapping[object] = numberOfGenerations - 1;

  lastGeneration.add(object);
}
```

`removeObject` 实现也比较简单，基本上就是把 `addObject` 的改动回滚下：

```cpp
void GenerationManager::removeObject(__unsafe_unretained id object) {
  auto it = generationMapping.find(object);
  if (it == generationMapping.end()) {
    return;
  }
  NSInteger generationNumber = it->second;
  // 根据 generationMapping 找到对象所对应的层级，然后找到对应的 Generation
  Generation &generation = generations[generationNumber];
  generation.remove(object);

  generationMapping.erase(object);
}
```

## 获取统计数据

当完成数据收集后，我们可以通过 `FBAllocationTrackerManager` 提供的接口来获取相关数据， `currentAllocationSummary` 可以获取当前所有的对象，而 `FBAllocationTrackerSummary` 也提供了相关的数据：

```objc
NSArray<FBAllocationTrackerSummary *> *summaries = [[FBAllocationTrackerManager sharedManager] currentAllocationSummary];

// FBAllocationTrackerSummary.h
@property (nonatomic, readonly) NSUInteger allocations;
@property (nonatomic, readonly) NSUInteger deallocations;
@property (nonatomic, readonly) NSInteger aliveObjects;
@property (nonatomic, copy, readonly, nonnull) NSString *className;
@property (nonatomic, readonly) NSUInteger instanceSize;
```

而 `FBAllocationTrackerSummary` 则是由 struct `SingleClassSummary` 转换而来的：

```objc
// AllocationSummary 定义
typedef std::unordered_map<Class, SingleClassSummary, ClassHashFunctor, ClassEqualFunctor> AllocationSummary;

// SingleClassSummary 定义
struct SingleClassSummary {
  NSUInteger allocations;
  NSUInteger deallocations;
  NSUInteger instanceSize;
};

- (NSArray<FBAllocationTrackerSummary *> *)currentAllocationSummary
{
  // 通过 AllocationTracker 来获取 AllocationSummary
  FB::AllocationTracker::AllocationSummary summary = FB::AllocationTracker::allocationTrackerSummary();
  NSMutableArray<FBAllocationTrackerSummary *> *array = [NSMutableArray new];

  // Allocation 是一个以 Class 为 key ， SingleClassSummary 为 value 的 unordered_map
  // 因此可以利用其 key he value 来生成 FBAllocationTrackerSummary
  for (const auto &item: summary) {
    FB::AllocationTracker::SingleClassSummary singleSummary = item.second;
    Class aCls = item.first;
    NSString *className = NSStringFromClass(aCls);

    FBAllocationTrackerSummary *summaryObject =
    [[FBAllocationTrackerSummary alloc] initWithAllocations:singleSummary.allocations
                                              deallocations:singleSummary.deallocations
                                               aliveObjects:singleSummary.allocations - singleSummary.deallocations
                                                  className:className
                                               instanceSize:singleSummary.instanceSize];
    [array addObject:summaryObject];
  }

  return array;
}
```

```objc
AllocationSummary allocationTrackerSummary() {
    TrackerMap allocationsUntilNow;
    TrackerMap deallocationsUntilNow;

    {
      std::lock_guard<std::mutex> l(*_lock);
      // 创建当前所对应的新的 TrackerMap
      allocationsUntilNow = TrackerMap(*_allocations);
      deallocationsUntilNow = TrackerMap(*_deallocations);
    }
    // Class 的 unordered_set ，记录所存活的对象对应的 Class
    std::unordered_set<
    __unsafe_unretained Class,
    FB::AllocationTracker::ClassHashFunctor,
    FB::AllocationTracker::ClassEqualFunctor> keys;

    for (const auto &kv: allocationsUntilNow) {
      keys.insert(kv.first);
    }

    for (const auto &kv: deallocationsUntilNow) {
      keys.insert(kv.first);
    }

    AllocationSummary summary;

    for (Class aCls: keys) {
      // 如果 alloc 的次数小于 dealloc 的次数，则表明该类在内存中的所有对象都已经释放，不需要处理
      if (allocationsUntilNow[aCls] - deallocationsUntilNow[aCls] <= 0) {
        continue;
      }
      // 生成 SingleClassSummary
      SingleClassSummary singleSummary = {
        .allocations = allocationsUntilNow[aCls],
        .deallocations = deallocationsUntilNow[aCls],
        .instanceSize = class_getInstanceSize(aCls),
      };

      summary[aCls] = singleSummary;
    }

    return summary;
  }
```

`FBAllocationTrackerManager` 也提供了根据 `Generation` 进行划分的接口：

```objc
/// GenerationSummary 定义为以 Class 为 key , 存活计数为 value
typedef std::unordered_map<Class, NSInteger, ClassHashFunctor, ClassEqualFunctor> GenerationSummary;

/// FullGenerationSummary 为基于不同层级的 Generation 生成的 vector<GenerationSummary>
typedef std::vector<GenerationSummary> FullGenerationSummary;

- (NSArray<NSArray<FBAllocationTrackerSummary *> *> *)currentSummaryForGenerations
{
  FB::AllocationTracker::FullGenerationSummary summary = FB::AllocationTracker::generationSummary();

  if (summary.size() == 0) {
    return nil;
  }

  NSMutableArray *array = [NSMutableArray new];

  for (const auto &generation: summary) {
    [array addObject:[self _getSingleGenerationSummary:generation]];
  }

  return array;
}
```

取出的 `FullGenerationSummary` 还不能直接使用，需要转化为 Objective-C 层级的对象：

```objc
- (NSArray<FBAllocationTrackerSummary *> *)_getSingleGenerationSummary:(const FB::AllocationTracker::GenerationSummary &)summary
{
  NSMutableArray *array = [NSMutableArray new];

  for (const auto &kv: summary) {
    // 如上所述，key 为 Class ， value 为存活计数
    FBAllocationTrackerSummary *summaryObject =
    [[FBAllocationTrackerSummary alloc] initWithAllocations:0
                                              deallocations:0
                                               aliveObjects:kv.second
                                                  className:NSStringFromClass(kv.first)
                                               instanceSize:class_getInstanceSize(kv.first)];

    [array addObject:summaryObject];
  }

  return array;
}
```

而 `FullGenerationSummary` 则由 `FBAllocationTracker` 负责生成：

```objc
FullGenerationSummary generationSummary() {
  std::lock_guard<std::mutex> l(*_lock);
  /// 如果 _generationManager 为 nil ，则表示没有开启 Generation 记录，直接返回一个空的 FullGenerationSummary
  if (_generationManager) {
    return _generationManager->summary();
  }
  return FullGenerationSummary {};
}

FullGenerationSummary GenerationManager::summary() const {
  FullGenerationSummary fullSummary;

  // 获取每个 Generation 的 summary （全部存活对象的计数），以 Class 为 key
  for (const auto &generation: generations) {
    fullSummary.push_back(generation.getSummary());
  }

  return fullSummary;
}

GenerationSummary Generation::getSummary() const {
  GenerationSummary summary;
  // 简单地遍历下 Generation 的 objects
  for (const auto &kv: objects) {
    Class aCls = kv.first;
    const GenerationList &list = kv.second;

    NSInteger count = list.size();

    summary[aCls] = count;
  }

  return summary;
}
```

## 其它

FBAllocationTracker 基于 Objective-C/C++ 进行混编，使用了不少 C++ 特性，比如说 [std::lock_guard - cppreference.com](https://en.cppreference.com/w/cpp/thread/lock_guard) 。这是一个很好的示例。不少追求性能的 Objective-C 开源库都有类似的操作，在对性能有要求的部分可以使用 C/C++ 来编写，提供给外部的接口和对象可以转为 Objective-C 。 FBAllocationTracker 是一个比较简单的库，支持的功能也比较简单，它只支持监听 Objective-C 的对象，不支持 C++/C 在堆上操作的对象，如果需要更全面的监控信息，可以考虑使用 [OOMDetector](https://github.com/Tencent/OOMDetector) ，当然能力越大责任也越大， OOMDetector 由于使用了 [fishhook](https://github.com/facebook/fishhook) 对 `alloc` 相关方法进行了 hook ，更加底层，且影响面更大，接入时需要更加小心和谨慎。 OOMDetector 的相关 hook 操作：[OOMDetector/CMallocHook.mm](https://github.com/Tencent/OOMDetector/blob/master/libOOMDetector/libOOMDetector/OOMDetector/QQLeak/hook/CMallocHook.mm) 。 通过 FBAllocationTracker 可以获取到存活的对象，结合 [FBRetainCycleDetector](https://github.com/facebook/FBRetainCycleDetector) 可以检测是否是循环引用导致的，[FBMemoryProfiler](https://github.com/facebookarchive/FBMemoryProfiler) 基于这两者提供了方便操作的 UI 视图。
