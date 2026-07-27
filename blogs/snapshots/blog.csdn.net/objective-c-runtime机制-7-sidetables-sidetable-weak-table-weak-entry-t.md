---
title: Objective-C runtime机制(7)——SideTables, SideTable, weak_table, weak_entry_t
source_url: 'https://blog.csdn.net/u013378438/article/details/82790332'
source_domain: blog.csdn.net
source_group: platform
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:13abc213e00db30f'
plan_ref: 第二周：weak、属性关键字与 Block / Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）
container: '//div[@id=''content_views'']'
container_source: map
---

> 原文：[Objective-C runtime机制(7)——SideTables, SideTable, weak_table, weak_entry_t](https://blog.csdn.net/u013378438/article/details/82790332)

在runtime中，有四个数据结构非常重要，分别是SideTables，SideTable，weak_table_t和weak_entry_t。它们和对象的引用计数，以及weak引用相关。

## 关系

先说一下这四个数据结构的关系。 在runtime内存空间中，`SideTables`是一个~~64个元素长度~~8个元素长度 的hash数组，里面存储了`SideTable`。`SideTables`的hash键值就是一个对象`obj`的`address`。  
 因此可以说，一个`obj`，对应了一个`SideTable`。但是一个`SideTable`，会对应多个`obj`。因为`SideTable`的数量只有64个，所以会有很多`obj`共用同一个`SideTable`。

而在一个`SideTable`中，又有两个成员，分别是

```
RefcountMap refcnts;        // 对象引用计数相关 map
weak_table_t weak_table;    // 对象弱引用相关 table
```

其中，`refcents`是一个hash map，其key是obj的地址，而value，则是obj对象的引用计数。

而`weak_table`则存储了弱引用obj的指针的地址，其本质是一个以obj地址为key，弱引用obj的指针的地址作为value的hash表。hash表的节点类型是`weak_entry_t`。

这四个数据结构的关系如下图：  
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3db3cb96de0c244b14d0c7d7ee40107b.png)

## SideTables

先来说一下最外层的`SideTables`。`SideTables`可以理解为一个全局的hash数组，里面存储了`SideTable`类型的数据，其长度为`64`。

`SideTabls`可以通过全局的静态函数获取：

```
static StripedMap<SideTable>& SideTables() {
    return *reinterpret_cast<StripedMap<SideTable>*>(SideTableBuf);
}
```

可以看到，`SideTabls` 实质类型为模板类型`StripedMap` 。`StripedMap`直译过来是“有条纹的Map”，不知道为什么叫做这个鸟名字。

### StripedMap

我们继续来看`StripedMap`模板的定义：

```
// StripedMap<T> is a map of void* -> T, sized appropriately 
// for cache-friendly lock striping. 
// For example, this may be used as StripedMap<spinlock_t>
// or as StripedMap<SomeStruct> where SomeStruct stores a spin lock.
template<typename T>
class StripedMap {

    enum { CacheLineSize = 64 };

#if TARGET_OS_EMBEDDED
    enum { StripeCount = 8 };
#else
    enum { StripeCount = 64 };  // iOS 设备的StripeCount = 64
#endif

    struct PaddedT {
        T value alignas(CacheLineSize); // T value 64字节对齐
        
    };

    PaddedT array[StripeCount]; // 所有PaddedT struct 类型数据被存储在array数组中。iOS 设备 StripeCount == 64

    static unsigned int indexForPointer(const void *p) { // 该方法以void *作为key 来获取void *对应在StripedMap 中的位置
        uintptr_t addr = reinterpret_cast<uintptr_t>(p);
        return ((addr >> 4) ^ (addr >> 9)) % StripeCount; // % StripeCount 防止index越界
    }

 public:
    // 取值方法 [p],
    T& operator[] (const void *p) { 
        return array[indexForPointer(p)].value; 
    }
    const T& operator[] (const void *p) const { 
        return const_cast<StripedMap<T>>(this)[p]; 
    }

    
    // Shortcuts for StripedMaps of locks.
    void lockAll() {
        for (unsigned int i = 0; i < StripeCount; i++) {
            array[i].value.lock();
        }
    }

    void unlockAll() {
        for (unsigned int i = 0; i < StripeCount; i++) {
            array[i].value.unlock();
        }
    }

    void forceResetAll() {
        for (unsigned int i = 0; i < StripeCount; i++) {
            array[i].value.forceReset();
        }
    }

    void defineLockOrder() {
        for (unsigned int i = 1; i < StripeCount; i++) {
            lockdebug_lock_precedes_lock(&array[i-1].value, &array[i].value);
        }
    }

    void precedeLock(const void *newlock) {
        // assumes defineLockOrder is also called
        lockdebug_lock_precedes_lock(&array[StripeCount-1].value, newlock);
    }

    void succeedLock(const void *oldlock) {
        // assumes defineLockOrder is also called
        lockdebug_lock_precedes_lock(oldlock, &array[0].value);
    }

    const void *getLock(int i) {
        if (i < StripeCount) return &array[i].value;
        else return nil;
    }
};
```

通过开头的英文注释，

> // StripedMap is a map of void* -\> T, sized appropriately

可以知道， `StripedMap` 是一个以`void *`为hash key， `T`为vaule的hash 表。  
 hash定位的算法如下：

```
    static unsigned int indexForPointer(const void *p) { // 该方法以void *作为key 来获取void *对应在StripedMap 中的位置
        uintptr_t addr = reinterpret_cast<uintptr_t>(p);
        return ((addr >> 4) ^ (addr >> 9)) % StripeCount; // % StripeCount 防止index越界
    }
```

把地址指针右移4位异或地址指针右移9位，为什么这么做，也不用关心。我们只要关心重点是最后的值要取余`StripeCount`，来防止index越界就好。

`StripedMap`的所有`T`类型数据都被封装到`PaddedT`中：

```
    struct PaddedT {
        T value alignas(CacheLineSize); // T value 64字节对齐
        
    };
```

之所以再次封装到`PaddedT` （有填充的T）中，是为了字节对齐，估计是存取hash值时的效率考虑。

接下来，这些`PaddedT`被放到数组`array`中：

```
 PaddedT array[StripeCount]; // 所有PaddedT struct 类型数据被存储在array数组中。iOS 设备 StripeCount == 64
```

然后，苹果为array数组写了一些公共的存取数据的方法，主要是调用`indexForPointer`方法，使得外部传入的`对象地址指针`直接hash到对应的array节点：

```
 // 取值方法 [p],
    T& operator[] (const void *p) { 
        return array[indexForPointer(p)].value; 
    }
    const T& operator[] (const void *p) const { 
        return const_cast<StripedMap<T>>(this)[p]; 
    }
```

接下来是一堆锁的操作，由于`SideTabls`是一个全局的hash表，因此当然必须要带锁访问。`StripedMap`提供了一些便捷的锁操作方法：

```
// Shortcuts for StripedMaps of locks.
    void lockAll() {
        for (unsigned int i = 0; i < StripeCount; i++) {
            array[i].value.lock();
        }
    }

    void unlockAll() {
        for (unsigned int i = 0; i < StripeCount; i++) {
            array[i].value.unlock();
        }
    }

    void forceResetAll() {
        for (unsigned int i = 0; i < StripeCount; i++) {
            array[i].value.forceReset();
        }
    }

    void defineLockOrder() {
        for (unsigned int i = 1; i < StripeCount; i++) {
            lockdebug_lock_precedes_lock(&array[i-1].value, &array[i].value);
        }
    }

    void precedeLock(const void *newlock) {
        // assumes defineLockOrder is also called
        lockdebug_lock_precedes_lock(&array[StripeCount-1].value, newlock);
    }

    void succeedLock(const void *oldlock) {
        // assumes defineLockOrder is also called
        lockdebug_lock_precedes_lock(oldlock, &array[0].value);
    }

    const void *getLock(int i) {
        if (i < StripeCount) return &array[i].value;
        else return nil;
    }
```

可以看到，所有的`StripedMap`锁操作，最终是调用的`array[i].value`的相关操作。因此，对于模板的抽象数据`T类型`，必须具备相关的lock操作接口。

因此，要用`StripedMap`作为模板hash表，对于T类型还是有所要求的。而在`SideTables`中，`T`即为`SideTable`类型，我们稍后会看到SideTable是如何符合StripedMap的数据类型要求的。

分析完了`StripedMap`, 也就分析完了`SideTables`这个全局的大hash表。现在就来继续分析SideTables中存储的数据，`SideTable`吧。

## SideTable

`SideTable` 翻译过来的意思是“边桌”，可以放一下小东西。这里，主要存放了OC对象的引用计数和弱引用相关信息。定义如下:

```
struct SideTable {
    spinlock_t slock;           // 自旋锁，防止多线程访问冲突
    RefcountMap refcnts;        // 对象引用计数map
    weak_table_t weak_table;    // 对象弱引用map

    SideTable() {
        memset(&weak_table, 0, sizeof(weak_table));
    }

    ~SideTable() {
        _objc_fatal("Do not delete SideTable.");
    }

    // 锁操作 符合StripedMap对T的定义
    void lock() { slock.lock(); }
    void unlock() { slock.unlock(); }
    void forceReset() { slock.forceReset(); }

    // Address-ordered lock discipline for a pair of side tables.

    template<HaveOld, HaveNew>
    static void lockTwo(SideTable *lock1, SideTable *lock2);
    template<HaveOld, HaveNew>
    static void unlockTwo(SideTable *lock1, SideTable *lock2);
};
```

`SideTable`的定义很清晰，有三个成员:

- `spinlock_t slock` : 自旋锁，用于上锁/解锁 SideTable。
- `RefcountMap refcnts` ：以`DisguisedPtr<objc_object>`为key的hash表，用来存储OC对象的引用计数(仅在未开启isa优化 或 在isa优化情况下isa_t的引用计数溢出时才会用到)。
- `weak_table_t weak_table` : 存储对象弱引用指针的hash表。是OC weak功能实现的核心数据结构。

除了三个成员外，苹果为`SideTable`还写了构造和析构函数：

```
// 构造函数
    SideTable() {
        memset(&weak_table, 0, sizeof(weak_table));
    }

    //析构函数(看看函数体，苹果设计的SideTable其实不希望被析构，不然会引起fatal 错误)
    ~SideTable() {
        _objc_fatal("Do not delete SideTable.");
    }
```

通过析构函数可以知道，`SideTable`是不能被析构的。

最后是一堆锁的操作，用于多线程访问`SideTable`， 同时，也符合我们上面提到的`StripedMap`中关于value的lock接口定义：

```
// 锁操作 符合StripedMap对T的定义
    void lock() { slock.lock(); }
    void unlock() { slock.unlock(); }
    void forceReset() { slock.forceReset(); }

    // Address-ordered lock discipline for a pair of side tables.

    template<HaveOld, HaveNew>
    static void lockTwo(SideTable *lock1, SideTable *lock2);
    template<HaveOld, HaveNew>
    static void unlockTwo(SideTable *lock1, SideTable *lock2);
```

### spinlock_t slock

`spinlock_t`的最终定义实际上是一个`uint32_t`类型的`非公平的自旋锁`。所谓非公平，就是说获得锁的顺序和申请锁的顺序无关，也就是说，第一个申请锁的线程有可能会是最后一个获得到该锁，或者是刚获得锁的线程会再次立刻获得到该锁，造成饥饿等待。 同时，在OC中，`_os_unfair_lock_opaque`也记录了获取它的线程信息，只有获得该锁的线程才能够解开这把锁。

```
typedef struct os_unfair_lock_s {
	uint32_t _os_unfair_lock_opaque;
} os_unfair_lock, *os_unfair_lock_t;
```

关于自旋锁的实现，苹果并未公布，但是大体上应该是通过操作`_os_unfair_lock_opaque` 这个`uint32_t`的值，当大于0时，锁可用，当等于或小于0时，需要锁等待。

### RefcountMap refcnts

`RefcountMap refcnts` 用来存储OC对象的引用计数。它实质上是一个以`objc_object`为key的hash表，其vaule就是OC对象的引用计数。同时，当OC对象的引用计数变为0时，会自动将相关的信息从hash表中剔除。`RefcountMap`的定义如下：

```
// RefcountMap disguises its pointers because we 
// don't want the table to act as a root for `leaks`.
typedef objc::DenseMap<DisguisedPtr<objc_object>,size_t,true> RefcountMap;
```

实质上是模板类型`objc::DenseMap`。模板的三个类型参数`DisguisedPtr<objc_object>`，`size_t`, `true` 分别表示`DenseMap`的hash key类型，value类型，是否需要在value==0的时候自动释放掉响应的hash节点，这里是true。

而`DenseMap`这个模板类型又继承与另一个Base 模板类型`DenseMapBase` ：

```
template<typename KeyT, typename ValueT,
         bool ZeroValuesArePurgeable = false, 
         typename KeyInfoT = DenseMapInfo<KeyT> >
class DenseMap
    : public DenseMapBase<DenseMap<KeyT, ValueT, ZeroValuesArePurgeable, KeyInfoT>,
                          KeyT, ValueT, KeyInfoT, ZeroValuesArePurgeable> 
```

关于`DenseMap`的定义，苹果写了一大坨，有些复杂，这里就不去深究了，有兴趣的同学可以自己去看下相关的源码部分。

### weak_table_t weak_table

重点来了，`weak_table_t weak_table` 用来存储OC对象弱引用的相关信息。我们知道，`SideTables`一共只有64个节点，而在我们的APP中，一般都会不只有64个对象，因此，多个对象一定会重用同一个`SideTable`节点，也就是说，一个`weak_table`会存储多个对象的弱引用信息。因此在一个`SideTable`中，又会通过`weak_table`作为hash表再次分散存储每一个对象的弱引用信息。

`weak_table_t`的定义如下：

```
/**
 * The global weak references table. Stores object ids as keys,
 * and weak_entry_t structs as their values.
 */
struct weak_table_t {
    weak_entry_t *weak_entries;        // hash数组，用来存储弱引用对象的相关信息weak_entry_t
    size_t    num_entries;             // hash数组中的元素个数
    uintptr_t mask;                    // hash数组长度-1，会参与hash计算。（注意，这里是hash数组的长度，而不是元素个数。比如，数组长度可能是64，而元素个数仅存了2个）
    uintptr_t max_hash_displacement;   // 可能会发生的hash冲突的最大次数，用于判断是否出现了逻辑错误（hash表中的冲突次数绝不会超过改值）
};
```

weak_table_t是一个典型的hash结构。其中 weak_entry_t *weak_entries是一个动态数组，用来存储weak_table_t的数据元素weak_entry_t。  
 剩下的三个元素将会用于hash表的相关操作。weak_table的hash定位操作如下所示：

```
static weak_entry_t *
weak_entry_for_referent(weak_table_t *weak_table, objc_object *referent)
{
    assert(referent);

    weak_entry_t *weak_entries = weak_table->weak_entries;

    if (!weak_entries) return nil;

    size_t begin = hash_pointer(referent) & weak_table->mask;  // 这里通过 & weak_table->mask的位操作，来确保index不会越界
    size_t index = begin;
    size_t hash_displacement = 0;
    while (weak_table->weak_entries[index].referent != referent) {
        index = (index+1) & weak_table->mask;
        if (index == begin) bad_weak_table(weak_table->weak_entries); // 触发bad weak table crash
        hash_displacement++;
        if (hash_displacement > weak_table->max_hash_displacement) { // 当hash冲突超过了可能的max hash 冲突时，说明元素没有在hash表中，返回nil 
            return nil;
        }
    }
    
    return &weak_table->weak_entries[index];
}
```

上面的定位操作还是比较清晰的，首先通过

```
 size_t begin = hash_pointer(referent) & weak_table->mask;
```

来尝试确定hash的初始位置。注意，这里做了`& weak_table->mask` 位操作来确保index不会越界，这同我们平时用到的`取余%`操作是一样的功能。只不过这里改用了位操作，提升了效率。

然后，就开始对比hash表中的数据是否与目标数据相等`while (weak_table->weak_entries[index].referent != referent)`，如果不相等，则`index +1`， 直到`index == begin`（绕了一圈）或超过了可能的`hash冲突最大值`。

这是weak_table_t如何进行hash定位的相关操作。

关于weak_table_t中如何添加/删除元素，我们在上一章[Objective-C runtime机制(6)——weak引用的底层实现原理](https://blog.csdn.net/u013378438/article/details/82767947)中已有分析，在这里我们不再展开。

### weak_entry_t

`weak_table_t`中存储的元素是`weak_entry_t`类型，每个`weak_entry_t`类型对应了一个OC对象的弱引用信息。

`weak_entry_t`的结构和`weak_table_t`很像，同样也是一个hash表，其存储的元素是`weak_referrer_t`，实质上是弱引用该对象的指针的指针，即 `objc_object **new_referrer` ， 通过操作指针的指针，就可以使得weak 引用的指针在对象析构后，指向nil。

```
// The address of a __weak variable.
// These pointers are stored disguised so memory analysis tools
// don't see lots of interior pointers from the weak table into objects.

typedef DisguisedPtr<objc_object *> weak_referrer_t;
```

`weak_entry_t` 的定义如下：

```
/**
 * The internal structure stored in the weak references table. 
 * It maintains and stores
 * a hash set of weak references pointing to an object.
 * If out_of_line_ness != REFERRERS_OUT_OF_LINE then the set
 * is instead a small inline array.
 */
#define WEAK_INLINE_COUNT 4

// out_of_line_ness field overlaps with the low two bits of inline_referrers[1].
// inline_referrers[1] is a DisguisedPtr of a pointer-aligned address.
// The low two bits of a pointer-aligned DisguisedPtr will always be 0b00
// (disguised nil or 0x80..00) or 0b11 (any other address).
// Therefore out_of_line_ness == 0b10 is used to mark the out-of-line state.
#define REFERRERS_OUT_OF_LINE 2

struct weak_entry_t {
    DisguisedPtr<objc_object> referent; // 被弱引用的对象
    
    // 引用该对象的对象列表，联合。 引用个数小于4，用inline_referrers数组。 用个数大于4，用动态数组weak_referrer_t *referrers
    union {
        struct {
            weak_referrer_t *referrers;                      // 弱引用该对象的对象指针地址的hash数组
            uintptr_t        out_of_line_ness : 2;           // 是否使用动态hash数组标记位
            uintptr_t        num_refs : PTR_MINUS_2;         // hash数组中的元素个数
            uintptr_t        mask;                           // hash数组长度-1，会参与hash计算。（注意，这里是hash数组的长度，而不是元素个数。比如，数组长度可能是64，而元素个数仅存了2个）素个数）。
            uintptr_t        max_hash_displacement;          // 可能会发生的hash冲突的最大次数，用于判断是否出现了逻辑错误（hash表中的冲突次数绝不会超过改值）
        };
        struct {
            // out_of_line_ness field is low bits of inline_referrers[1]
            weak_referrer_t  inline_referrers[WEAK_INLINE_COUNT];
        };
    };

    bool out_of_line() {
        return (out_of_line_ness == REFERRERS_OUT_OF_LINE);
    }

    weak_entry_t& operator=(const weak_entry_t& other) {
        memcpy(this, &other, sizeof(other));
        return *this;
    }

    weak_entry_t(objc_object *newReferent, objc_object **newReferrer)
        : referent(newReferent) // 构造方法，里面初始化了静态数组
    {
        inline_referrers[0] = newReferrer;
        for (int i = 1; i < WEAK_INLINE_COUNT; i++) {
            inline_referrers[i] = nil;
        }
    }
};
```

weak_entry_t的结构也比较清晰：

- `DisguisedPtr<objc_object> referent` ：弱引用对象指针摘要。其实可以理解为弱引用对象的指针，只不过这里使用了摘要的形式存储。（所谓摘要，其实是把地址取负）。
- `union` ：接下来是一个联合，union有两种形式：`定长数组weak_referrer_t inline_referrers[WEAK_INLINE_COUNT]` 和 `动态数组 weak_referrer_t *referrers`。这两个数组是用来存储弱引用该对象的指针的指针的，同样也使用了指针摘要的形式存储。当弱引用该对象的指针数目小于等于`WEAK_INLINE_COUNT`时，使用定长数组。当超过`WEAK_INLINE_COUNT`时，会将定长数组中的元素转移到动态数组中，并之后都是用动态数组存储。关于`定长数组/动态数组 切换`这部分，我们在稍后详细分析。
- `bool out_of_line()`： 该方法用来判断当前的`weak_entry_t`是使用的定长数组还是动态数组。当返回`true`，此时使用的动态数组，当返回`false`，使用静态数组。
- `weak_entry_t& operator=(const weak_entry_t& other)` ：赋值方法
- `weak_entry_t(objc_object *newReferent, objc_object **newReferrer)` ：构造方法。

### 定长数组 / 动态数组

`weak_entry_t`会存储所有弱引用该对象的指针的指针。存储类型为`weak_referrer_t` ，其实就是弱引用指针的指针。但是是以指针摘要的形式存储的：

```
typedef DisguisedPtr<objc_object *> weak_referrer_t;
```

`weak_entry_t`会将`weak_referrer_t`存储到hash数组中，而这个hash数组会有两种形态：定长数组/动态数组：

```
   union {
   		// 动态数组模式
        struct {
            weak_referrer_t *referrers;                      // 弱引用该对象的对象指针地址的hash数组
            uintptr_t        out_of_line_ness : 2;           // 是否使用动态hash数组标记位
            uintptr_t        num_refs : PTR_MINUS_2;         // hash数组中的元素个数
            uintptr_t        mask;                           // hash数组长度-1，会参与hash计算。（注意，这里是hash数组的长度，而不是元素个数。比如，数组长度可能是64，而元素个数仅存了2个）素个数）。
            uintptr_t        max_hash_displacement;          // 可能会发生的hash冲突的最大次数，用于判断是否出现了逻辑错误（hash表中的冲突次数绝不会超过改值）
        };
	  // 定长数组模式
        struct {
            // out_of_line_ness field is low bits of inline_referrers[1]
            weak_referrer_t  inline_referrers[WEAK_INLINE_COUNT];
        };
    };

    bool out_of_line() {
        return (out_of_line_ness == REFERRERS_OUT_OF_LINE);
    }
```

当弱引用指针个数少于等于`WEAK_INLINE_COUNT`时，会使用定长数组`inline_referrers`。而当大于`WEAK_INLINE_COUNT`时，则会转换到动态数组模式 `weak_referrer_t *referrers`。

之所以做定长/动态数组的切换，应该是苹果考虑到弱引用的指针个数一般不会超过`WEAK_INLINE_COUNT`个。这时候使用定长数组，不需要动态的申请内存空间，而是一次分配一块连续的内存空间。这会得到运行效率上的提升。

至于`weak_entry_t` 是使用的定长/动态数组，苹果提供了方法：

```
#define REFERRERS_OUT_OF_LINE 2

    bool out_of_line() {
        return (out_of_line_ness == REFERRERS_OUT_OF_LINE);
    }
```

该方法的实质是测试定长数组第二个元素值的2进制位第2位是否等于`01`。因为根据苹果的注释，`inline_referrers[1]` 中存储的是`pointer-aligned DisguisedPtr` ，即指针对齐的指针摘要，其最低位一定是`0b00`或`0b11`，因此可以用`0b10` 表示使用了动态数组。

下面我就来看一下`weak_entry_t` 中是如何插入元素的：

```
/** 
 * Add the given referrer to set of weak pointers in this entry.
 * Does not perform duplicate checking (b/c weak pointers are never
 * added to a set twice). 
 *
 * @param entry The entry holding the set of weak pointers. 
 * @param new_referrer The new weak pointer to be added.
 */
static void append_referrer(weak_entry_t *entry, objc_object **new_referrer)
{
    if (! entry->out_of_line()) { // 如果weak_entry 尚未使用动态数组，走这里
        // Try to insert inline.
        for (size_t i = 0; i < WEAK_INLINE_COUNT; i++) {
            if (entry->inline_referrers[i] == nil) {
                entry->inline_referrers[i] = new_referrer;
                return;
            }
        }
        
        // 如果inline_referrers的位置已经存满了，则要转型为referrers，做动态数组。
        // Couldn't insert inline. Allocate out of line.
        weak_referrer_t *new_referrers = (weak_referrer_t *)
            calloc(WEAK_INLINE_COUNT, sizeof(weak_referrer_t));
        // This constructed table is invalid, but grow_refs_and_insert
        // will fix it and rehash it.
        for (size_t i = 0; i < WEAK_INLINE_COUNT; i++) {
            new_referrers[i] = entry->inline_referrers[i];
        }
        entry->referrers = new_referrers;
        entry->num_refs = WEAK_INLINE_COUNT;
        entry->out_of_line_ness = REFERRERS_OUT_OF_LINE;
        entry->mask = WEAK_INLINE_COUNT-1;
        entry->max_hash_displacement = 0;
    }

    // 对于动态数组的附加处理：
    assert(entry->out_of_line()); // 断言： 此时一定使用的动态数组

    if (entry->num_refs >= TABLE_SIZE(entry) * 3/4) { // 如果动态数组中元素个数大于或等于数组位置总空间的3/4，则扩展数组空间为当前长度的一倍
        return grow_refs_and_insert(entry, new_referrer); // 扩容，并插入
    }
    
    // 如果不需要扩容，直接插入到weak_entry中
    // 注意，weak_entry是一个哈希表，key：w_hash_pointer(new_referrer) value: new_referrer
    
    // 细心的人可能注意到了，这里weak_entry_t 的hash算法和 weak_table_t的hash算法是一样的，同时扩容/减容的算法也是一样的
    size_t begin = w_hash_pointer(new_referrer) & (entry->mask); // '& (entry->mask)' 确保了 begin的位置只能大于或等于 数组的长度
    size_t index = begin;  // 初始的hash index
    size_t hash_displacement = 0;  // 用于记录hash冲突的次数，也就是hash再位移的次数
    while (entry->referrers[index] != nil) {
        hash_displacement++;
        index = (index+1) & entry->mask;  // index + 1, 移到下一个位置，再试一次能否插入。（这里要考虑到entry->mask取值，一定是：0x111, 0x1111, 0x11111, ... ，因为数组每次都是*2增长，即8， 16， 32，对应动态数组空间长度-1的mask，也就是前面的取值。）
        if (index == begin) bad_weak_table(entry); // index == begin 意味着数组绕了一圈都没有找到合适位置，这时候一定是出了什么问题。
    }
    if (hash_displacement > entry->max_hash_displacement) { // 记录最大的hash冲突次数, max_hash_displacement意味着: 我们尝试至多max_hash_displacement次，肯定能够找到object对应的hash位置
        entry->max_hash_displacement = hash_displacement;
    }
    // 将ref存入hash数组，同时，更新元素个数num_refs
    weak_referrer_t &ref = entry->referrers[index];
    ref = new_referrer;
    entry->num_refs++;
}
```

代码可以分成两部分理解，一部分是使用定长数组的情况：

```
  if (! entry->out_of_line()) { // 如果weak_entry 尚未使用动态数组，走这里
        // Try to insert inline.
        for (size_t i = 0; i < WEAK_INLINE_COUNT; i++) {
            if (entry->inline_referrers[i] == nil) {
                entry->inline_referrers[i] = new_referrer;
                return;
            }
        }
        
        // 如果inline_referrers的位置已经存满了，则要转型为referrers，做动态数组。
        // Couldn't insert inline. Allocate out of line.
        weak_referrer_t *new_referrers = (weak_referrer_t *)
            calloc(WEAK_INLINE_COUNT, sizeof(weak_referrer_t));
        // This constructed table is invalid, but grow_refs_and_insert
        // will fix it and rehash it.
        for (size_t i = 0; i < WEAK_INLINE_COUNT; i++) {
            new_referrers[i] = entry->inline_referrers[i];
        }
        entry->referrers = new_referrers;
        entry->num_refs = WEAK_INLINE_COUNT;
        entry->out_of_line_ness = REFERRERS_OUT_OF_LINE;
        entry->mask = WEAK_INLINE_COUNT-1;
        entry->max_hash_displacement = 0;
    }
```

定长数组的逻辑很简单，直接安装数组顺序，将`new_referrer`插入即可。如果定长数组已经用尽，则将定长数组转型为动态数组：

```
weak_referrer_t *new_referrers = (weak_referrer_t *)
            calloc(WEAK_INLINE_COUNT, sizeof(weak_referrer_t));
...

entry->referrers = new_referrers; // hash数组由 entry->inline_referrers转换为 entry->referrers
```

要注意，定长数组转换为动态数组后，新的元素并没有插入到数组中，而仅是将原来定长数组中的内容转移到了动态数组中。新元素的插入逻辑，在下面动态数组部分：

```
    ...
    // 对于动态数组的附加处理：
    assert(entry->out_of_line()); // 断言： 此时一定使用的动态数组

    if (entry->num_refs >= TABLE_SIZE(entry) * 3/4) { // 如果动态数组中元素个数大于或等于数组位置总空间的3/4，则扩展数组空间为当前长度的一倍
        return grow_refs_and_insert(entry, new_referrer); // 扩容，并插入
    }
    
    // 如果不需要扩容，直接插入到weak_entry中
    // 注意，weak_entry是一个哈希表，key：w_hash_pointer(new_referrer) value: new_referrer
    
    // 细心的人可能注意到了，这里weak_entry_t 的hash算法和 weak_table_t的hash算法是一样的，同时扩容/减容的算法也是一样的
    size_t begin = w_hash_pointer(new_referrer) & (entry->mask); // '& (entry->mask)' 确保了 begin的位置只能大于或等于 数组的长度
    size_t index = begin;  // 初始的hash index
    size_t hash_displacement = 0;  // 用于记录hash冲突的次数，也就是hash再位移的次数
    while (entry->referrers[index] != nil) {
        hash_displacement++;
        index = (index+1) & entry->mask;  // index + 1, 移到下一个位置，再试一次能否插入。（这里要考虑到entry->mask取值，一定是：0x111, 0x1111, 0x11111, ... ，因为数组每次都是*2增长，即8， 16， 32，对应动态数组空间长度-1的mask，也就是前面的取值。）
        if (index == begin) bad_weak_table(entry); // index == begin 意味着数组绕了一圈都没有找到合适位置，这时候一定是出了什么问题。
    }
    if (hash_displacement > entry->max_hash_displacement) { // 记录最大的hash冲突次数, max_hash_displacement意味着: 我们尝试至多max_hash_displacement次，肯定能够找到object对应的hash位置
        entry->max_hash_displacement = hash_displacement;
    }
    // 将ref存入hash数组，同时，更新元素个数num_refs
    weak_referrer_t &ref = entry->referrers[index];
    ref = new_referrer;
    entry->num_refs++;
}
```

其实这部分的逻辑和weak_table_t中插入weak_entry_t是非常类似的。都使用了mask取余来解决hash冲突。

我们可以再细看一下动态数组是如何动态扩容的：

```
   if (entry->num_refs >= TABLE_SIZE(entry) * 3/4) { // 如果动态数组中元素个数大于或等于数组位置总空间的3/4，则扩展数组空间为当前长度的一倍
        return grow_refs_and_insert(entry, new_referrer); // 扩容，并插入
    }
```

```
/** 
 * Grow the entry's hash table of referrers. Rehashes each
 * of the referrers.
 * 
 * @param entry Weak pointer hash set for a particular object.
 */
__attribute__((noinline, used))
static void grow_refs_and_insert(weak_entry_t *entry, 
                                 objc_object **new_referrer)
{
    assert(entry->out_of_line());

    size_t old_size = TABLE_SIZE(entry);
    size_t new_size = old_size ? old_size * 2 : 8; // 每次扩容为上一次容量的2倍

    size_t num_refs = entry->num_refs;
    weak_referrer_t *old_refs = entry->referrers;
    entry->mask = new_size - 1;
    
    entry->referrers = (weak_referrer_t *)
        calloc(TABLE_SIZE(entry), sizeof(weak_referrer_t));
    entry->num_refs = 0;
    entry->max_hash_displacement = 0;
    
    // 这里可以看到，旧的数据需要依次转移到新的内存中
    for (size_t i = 0; i < old_size && num_refs > 0; i++) {
        if (old_refs[i] != nil) {
            append_referrer(entry, old_refs[i]); // 将旧的数据转移到新的动态数组中
            num_refs--;
        }
    }
    // Insert
    append_referrer(entry, new_referrer);
    if (old_refs) free(old_refs); // 释放旧的内存
}
```

通过代码可以看出，每一次动态数组的扩容，都需要将旧的数据重新插入到新的数组中。

## 总结

OK，上面就是在runtime中，关于对象引用计数和weak引用相关的数据结构。搞清楚了它们之间的关系以及各自的实现细节，相信大家会对runtime有更深的理解。
