---
title: 绕过 objc_msgSend
source: Saagar Jha
source_key: saagarjha
source_url: 'https://saagarjha.com/blog/2019/12/15/bypassing-objc-msgsend/'
original_language: en
published: 2019-12-15
status: active
license: CC BY-SA 4.0 → 可再分发，但译文必须同样 BY-SA 并署名
archived_at: 2026-07-27
content_hash: 'sha256:49cea6adc34fea8f'
translated: true
---

> 原文：[Bypassing objc_msgSend](https://saagarjha.com/blog/2019/12/15/bypassing-objc-msgsend/)　·　Saagar Jha

# 绕过 `objc_msgSend`

2019 年 12 月 15 日，星期日

在最快路径上，[`objc_msgSend`](https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend) 可以在十几个指令内将执行权转移到 [`IMP`](https://developer.apple.com/documentation/objectivec/objective-c_runtime/imp)：

```
$ otool -tV /usr/lib/libobjc.dylib -p _objc_msgSend | head -n 18
/usr/lib/libobjc.dylib:
(__TEXT,__text) section
_objc_msgSend:
0000000000006e00	testq	%rdi, %rdi
0000000000006e03	je	0x6e78
0000000000006e06	testb	$0x1, %dil
0000000000006e0a	jne	0x6e83
0000000000006e0d	movabsq	$_objc_absolute_packed_isa_class_mask, %r10
0000000000006e17	andq	__objc_empty_vtable(%rdi), %r10
0000000000006e1a	movq	%rsi, %r11
0000000000006e1d	andl	0x18(%r10), %r11d
0000000000006e21	shlq	$0x4, %r11
0000000000006e25	addq	0x10(%r10), %r11
0000000000006e29	cmpq	__objc_empty_vtable(%r11), %rsi
0000000000006e2c	jne	0x6e38
0000000000006e2e	movq	0x8(%r11), %r11
0000000000006e32	xorq	%r10, %r11
0000000000006e35	jmpq	*%r11
```

作为系统上最热（如果不是最热的话）的代码路径之一，它如此优化是有充分理由的：即使是最微小的改进也能直接转化为所有 Objective‑C App 上可衡量的性能提升。但即使这个实现已经很快，有时仍然不够：Objective‑C 是一种动态语言，它的特性即便你没有使用也要付出代价。典型 `objc_msgSend` 调用中执行的大部分代码并非用于实现查找，而是检查执行能否走快速路径。但这些检查相对廉价：更大的问题是该函数在很大程度上充当了编译器的优化屏障——在编译器看来，它不过是一个通向未知目标的不可穿透的蹦床。因此，即使是最简单的成员访问也无法内联；每个方法调用都*必须*破坏多个寄存器，并且几乎总是需要将结果从累加器中移出——通常我们不希望把结果留在那里。

[`__attribute__((objc_direct))`](https://github.com/llvm/llvm-project/commit/d4e1ba3fa9dfec2613bdcc7db0b58dea490c56b1)（以及密切相关的 `__attribute__((objc_direct_members))`）试图通过将方法调用转换为本质上属于 C 风格的静态派发来解决其中一些问题。这一改动在引入时引发了一些争议：调用将不再经过 runtime 机制，从而破坏了 Objective‑C 的许多特性，包括方法交换（swizzling）、KVO，甚至子类化（subclassing）。幸运的是，还有另一种方法可以在不失去 Objective‑C 一些最佳特性的情况下获得性能优势。

## 一点闲散的推测

关键的洞察在于，我们可以猜测绝大多数方法调用的目标，并且可以在_编译时_仅通过查看接收者的类型和发送给它的消息来做到这一点。大多数情况下，`objc_msgSend` 只是在确认我们已经知道的事情：它的快速路径与直接函数调用之间的唯一实际区别是，在跳转到目标之前，它需要尽可能快地检查目标是否如预期。如果我们想支持 Objective‑C 的动态性，这是无法绕开的；我们提出的任何实现都必须做同样的事。相比于 `objc_msgSend`，我们的优势在于，作为人类（或作为编译器），我们拥有静态类型信息和对周围代码的理解，这使我们能够静态且高精度地猜测目标是什么。事实上，我们完全可以_推测_调用将前往预测的方法，并且借鉴 `objc_msgSend` 的做法，用最少的检查包装对该方法的直接调用，以确保我们的预测正确。用伪代码表示，我们可以将对 `-[Foo bar]` 的调用（接收者是 `foo`）转换为如下形式：

```
if (target is -[Foo bar]) {
	jump to -[Foo bar]
} else {
	objc_msgSend(foo, @selector(bar))
}
```

如果我们预测正确，这不仅跳过了 `objc_msgSend` 执行的缓存查找，而且还对方法进行了_直接_调用——编译器知道这个调用并可以围绕它进行优化。

## 跳转到实现

我们几乎完成了：唯一剩下的问题是“target is `-[Foo bar]`”条件中要放什么。据我所知，如果我们有一个 `Foo *foo` 并向其发送 `@selector(bar)`，执行不会直接进入 `-[Foo bar]` 的情况只有：

1. 接收者为 `nil`，
2. 接收者是 `Foo` 的子类（subclass），或
3. `-[Foo bar]` 被 swizzled 了。

检查第一种情况很容易做到；第二种稍微复杂一些。理论上我们问的是 `[foo isMemberOfClass:Foo.class]`，但出于显而易见的原因，我们并不真正想要由此带来的开销。我们可以连 [`object_getClass`](https://developer.apple.com/documentation/objectivec/1418629-object_getclass?language=objc) 的调用都跳过，直接提取 `foo` 的 `isa` 并与 runtime 元数据进行比较。这里有一些关于[非指针 isa（non-pointer isa）](http://www.sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html)和[标记指针（tagged pointer）](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)的微妙之处，但我们可以通过适当地屏蔽 `isa` 来完全避免它们，并在遇到非标准情况时将非标准情况送交慢速路径处理。

最后一种情况，即方法已被 swizzled，无法仅凭 `objc_msgSend` 可用的信息来确定：相反，我们需要维护一个布尔值的辅助表，每次调用都必须检查该表。当方法被 swizzled 时，runtime（或插入到 runtime 前面的你的代码）必须更新相应的条目，以便后续调用走 runtime。

所有检查到位后，我们现在可以直接调用该方法。为了试验这一点，[我修改了 Clang](https://github.com/saagarjha/expresscall)，使其在原本发出简单消息发送时改为发出执行上述操作的 LLVM IR。我以前从未接触过 LLVM 项目，所以我的实现很笨拙，可能也不正确；不过，它对于我测试过的简单程序运行良好，如果你喜欢编译 LLVM，可以亲自尝试。因为我需要一个不是“llvm-project”的仓库名，故我将此技术命名为“expresscall”——就像“打一通加急电话”（making an expresscall）一样。“swiftcall”会更短，但造成混淆的可能性要大得多。

## 我们够快了吗？

没有比高度合成的基准测试更好的方法来衡量优化有多快（或有多慢）了。这个基准测试创建了一个简单的整数型 Objective‑C 数组类型，用随机数填充它，然后求和。因为我是一个可怕的人，所以你得滚动过去看它：

```
@import Foundation;
@import ObjectiveC;
#import <algorithm>
#import <array>
#import <chrono>
#import <dlfcn.h>
#import <iostream>
#import <random>
#import <type_traits>
#import <unordered_map>
#import <utility>

const auto benchmark_size = 1000000;
const auto trials = 100;

@interface IntegerArray : NSObject
- (instancetype)initWithNumbers:(NSUInteger *)numbers count:(NSUInteger)count;
- (NSUInteger)count;
- (NSUInteger)numberAtIndex:(NSUInteger)index;
- (NSUInteger)direct_count __attribute__((objc_direct));
- (NSUInteger)direct_numberAtIndex:(NSUInteger)index __attribute__((objc_direct));
- (NSUInteger)swizzled_count;
- (NSUInteger)swizzled_numberAtIndex:(NSUInteger)index;
@end

@implementation IntegerArray {
	NSUInteger *_numbers;
	NSUInteger _count;
}

- (instancetype)initWithNumbers:(NSUInteger *)numbers count:(NSUInteger)count {
	if (self = [super init]) {
		_numbers = numbers;
		_count = count;
	}
	return self;
}

- (NSUInteger)count {
	return _count;
}

- (NSUInteger)numberAtIndex:(NSUInteger)index {
	return _numbers[index];
}

- (NSUInteger)direct_count {
	return _count;
}

- (NSUInteger)direct_numberAtIndex:(NSUInteger)index {
	return _numbers[index];
}

- (NSUInteger)swizzled_count {
	return 0;
}

- (NSUInteger)swizzled_numberAtIndex:(NSUInteger)index {
	return index;
}
@end

enum Benchmark {
	expresscall = 0,
	message_send,
	direct,
	swizzled_expresscall,
	swizzled_message_send,
	_end
};

auto measure(Benchmark benchmark, std::mt19937 &generator) {
	std::array<NSUInteger, benchmark_size> numbers;
	std::uniform_int_distribution<NSUInteger> distribution(0, NSUIntegerMax / benchmark_size);
	std::generate(numbers.begin(), numbers.end(), [&]() {
		return distribution(generator);
	});
	IntegerArray *array = [[IntegerArray alloc] initWithNumbers:numbers.data() count:numbers.size()];
	NSUInteger sum = 0;
	auto time = std::chrono::system_clock::now();
	switch (benchmark) {
	case Benchmark::expresscall:
		for (NSUInteger i = 0; i < array.count; ++i) {
			sum += [array numberAtIndex:i];
		}
		break;
	case Benchmark::message_send:
		for (NSUInteger i = 0; i < reinterpret_cast<NSUInteger (*)(IntegerArray *, SEL)>(objc_msgSend)(array, @selector(count)); ++i) {
			sum += reinterpret_cast<NSUInteger (*)(IntegerArray *, SEL, NSUInteger)>(objc_msgSend)(array, @selector(numberAtIndex:), i);
		}
		break;
	case Benchmark::direct:
		for (NSUInteger i = 0; i < array.direct_count; ++i) {
			sum += [array direct_numberAtIndex:i];
		}
		break;
	case Benchmark::swizzled_expresscall:
		for (NSUInteger i = 0; i < array.swizzled_count; ++i) {
			sum += [array swizzled_numberAtIndex:i];
		}
		break;
	case Benchmark::swizzled_message_send:
		for (NSUInteger i = 0; i < reinterpret_cast<NSUInteger (*)(IntegerArray *, SEL)>(objc_msgSend)(array, @selector(swizzled_count)); ++i) {
			sum += reinterpret_cast<NSUInteger (*)(IntegerArray *, SEL, NSUInteger)>(objc_msgSend)(array, @selector(swizzled_numberAtIndex:), i);
		}
		break;
	default:
		assert(false);
	}
	// 通过返回总和确保程序确实执行了计算
	return std::make_pair(std::chrono::duration_cast<std::chrono::microseconds>(std::chrono::system_clock::now() - time), sum);
}

int main(void) {
	// 将空方法 swizzle 为指向实际实现
	auto IntegerArray_count = class_getInstanceMethod(IntegerArray.class, @selector(count));
	class_replaceMethod(IntegerArray.class, @selector(swizzled_count), method_getImplementation(IntegerArray_count), method_getTypeEncoding(IntegerArray_count));
	*static_cast<bool *>(dlsym(dlopen(NULL, RTLD_LAZY), "OBJC_EXPRESSCALL____IntegerArray_swizzled_count_")) = true;
	auto IntegerArray_numberAtIndex_ = class_getInstanceMethod(IntegerArray.class, @selector(numberAtIndex:));
	class_replaceMethod(IntegerArray.class, @selector(swizzled_numberAtIndex:), method_getImplementation(IntegerArray_numberAtIndex_), method_getTypeEncoding(IntegerArray_numberAtIndex_));
	*static_cast<bool *>(dlsym(dlopen(NULL, RTLD_LAZY), "OBJC_EXPRESSCALL____IntegerArray_swizzled_numberAtIndex__")) = true;

	std::array<Benchmark, Benchmark::_end * trials> benchmarks;
	std::unordered_map<Benchmark, std::chrono::microseconds> times;
	std::random_device random;
	std::mt19937 generator(random());

	for (auto i = 0; i != Benchmark::_end; ++i) {
		std::fill(benchmarks.begin() + i * trials, benchmarks.begin() + (i + 1) * trials, Benchmark(i));
		times[Benchmark(i)] = std::chrono::microseconds(0);
	}
	// 随机化运行基准测试迭代的顺序
	std::shuffle(benchmarks.begin(), benchmarks.end(), generator);

	std::cout << "Benchmarking average time to sum " << benchmark_size << " numbers (over " << trials << " trials)…" << std::endl;

	for (auto benchmark : benchmarks) {
		times[benchmark] += measure(benchmark, generator).first;
	}

	auto names = {"expresscall", "objc_msgSend", "objc_direct", "swizzled expresscall", "swizzled objc_msgSend"};
	for (auto i = 0; i != Benchmark::_end; ++i) {
		std::cout << *(names.begin() + i) << ": " << times[Benchmark(i)].count() / trials << "µs" << std::endl;
	}
	return 0;
}
```

我们测量了优化实现和普通方法调用（通过直接调用 `objc_msgSend` 模拟，以防止编译器将其转换为优化形式）完成该操作所花费的时间。为了更全面，我们还加入了一个 `__attribute__((objc_direct))` 实现，以及另外两个测试的 swizzled 版本（其中我们模拟了 runtime 为 expresscall 设置标志，以指示它应放弃尝试直接调用方法）。最后，以一种听起来合理但可能误入歧途的尝试来防止 CPU 的分支预测器或缓存搞鬼，我们随机化了测试的顺序。在我的计算机——一台配备 [Intel(R) Core(TM) i5-5287U CPU @ 2.90GHz](https://ark.intel.com/content/www/us/en/ark/products/84988/intel-core-i5-5287u-processor-3m-cache-up-to-3-30-ghz.html) 的 [MacBook Pro（Retina，13 英寸，2015 年初）](https://support.apple.com/kb/SP715?locale=en_US)上，结果如下：

```
build$ bin/clang++ expresscall_benchmark.mm -o expresscall_benchmark -O3 -isysroot "$(xcrun --show-sdk-path)" -isystem "$(xcode-select -p)/CommandLineTools/usr/include/c++/v1" -isystem "$(xcode-select -p)/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1" -fmodules -fcxx-modules -framework Foundation
build$ ./expresscall_benchmark
Benchmarking average time to sum 1000000 numbers (over 100 trials)…
expresscall: 1965µs
objc_msgSend: 8817µs
direct: 615µs
swizzled expresscall: 6337µs
swizzled objc_msgSend: 5130µs
```

结果需要一些解释，但很明显，expresscall 显著快于除了通过标记为 `__attribute__((objc_direct))` 的方法进行的调用之外的所有方式。编译器已经成功内联了这两个实现的函数体，因此它们之间的时间差就是检查 expresscall 目标是否有效的开销：每次试验 1.5 微秒，相当于每次方法调用约三分之二纳秒。swizzled 的 `objc_msgSend` 走该函数的最快路径，每次调用带来 2 纳秒的开销；swizzled 的 expresscall 也是这样，但额外检查造成了差异。未 swizzled 的 `objc_msgSend` 耗时更长，因为 `count` 和 `numberAtIndex:` 选择器（selector）在方法缓存查找中发生了冲突，导致需要额外的扫描。

## 未来的扩展

当 expresscall 的推测成立时——理想情况下几乎总是如此——它轻松胜过 `objc_msgSend`。尽管尚未经过特别优化，它的分支高度可预测，我预计现代 CPU 应该能够提前推测它的内存访问。由于当前实现在代码大小和内存使用方面略有代价，因此可能值得修改前端实现，选择性地应用 expresscall 优化：或许可以结合配置文件引导优化（profile-guided optimization）信息来增强它。通过额外的 runtime 支持，即使是慢速的 swizzled 情况也可以高效执行——毕竟我们执行的检查正是 `objc_msgSend` 顶部所做的那些，因此我们也许可以跳过其中一些。最后，为了节省空间，可以将这些检查提取到它们自己的简短函数中；如果不需要内联的好处，仍然有可能通过在调用检查函数之前将推测目标压入栈来实现性能提升，这样检查函数可以有条件地尾调用到该目标或 `objc_msgSend`。
