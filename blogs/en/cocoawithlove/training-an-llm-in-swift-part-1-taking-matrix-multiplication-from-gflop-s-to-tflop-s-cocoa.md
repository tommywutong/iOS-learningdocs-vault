---
title: 'Training an LLM in Swift, Part 1: Taking matrix multiplication from Gflop/s to Tflop/s | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:8a19cfee1ad42d16'
translated: false
---

> 原文：[Training an LLM in Swift, Part 1: Taking matrix multiplication from Gflop/s to Tflop/s | Cocoa with Love](https://www.cocoawithlove.com/blog/matrix-multiplications-swift.html)　·　Cocoa with Love (Matt Gallagher)

In this article, I try to get my own handwritten matrix multiplication code running as fast as possible for training a Large Language Model (LLM) in Swift. The aim is to give some insight into the key steps for optimizing mathematics code in Swift. I also hope that these examples will offer a sense of scale about the capabilities of the different units on Apple Silicon – CPU, SIMD, AMX and GPU.

This will be the first in a series where I look at training neural networks in Swift on Apple Silicon. Future articles will look at the _maybe-too-many_ frameworks Apple offer for machine learning on the Mac. Those established frameworks are what you should really use for matrix multiplication and machine learning (they’ve spent a few more years optimizing matrix kernels than I have).

But until then, I’m having fun writing everything for myself in a “no frameworks, no libraries” plain code approach.

And I’m not just writing matrix multiplication kernels. The sample app will use these kernels as part of a full LLM implementation and the numbers I’ll quote will be for entire forward and backward training iterations. The reference implementation for this series will be Andrej Karpathy’s [llm.c](https://github.com/karpathy/llm.c) (a plain C implementation of a GPT2-compatible model). It’s a fairly basic model but it does contain all the necessary components and is representative of real-world workloads.

That means it’s time for my favorite game: optimize Swift until it’s faster than C.

## Backstory

About two years ago, I dug up my engineering thesis from the early 2000s. It’s an image recognizer written in C++ that uses a neural network for classifying images. I wanted to get my old code running again but I hadn’t worked on ML code in a long time. It got annoying and I gave up.

For all the discussion around LLMs in early 2024, it felt like no one was _training_ neural networks on the Mac. At least, not in languages like Swift. I played with some Python libraries like PyTorch and TensorFlow but Python never does the calculations itself – it operates more like an orchestrator of another computational engine under the hood – and the separation left me feeling like I wasn’t in control.

A month later, Andrej Karpathy released [llm.c](https://github.com/karpathy/llm.c). This reached me in a way that other machine learning content didn’t because nothing is hidden. It is around 1000 lines of plain C and (although it’s filled with some pretty cryptic variable names) it’s relatively readable.

So naturally, I immediately rewrote it in Swift. And it was a lot of fun to play with.

Of course, playing with the code required some work to make it run fast. Some foreshadowing, here: the initial Swift implementation was really super slow. But optimization is a constant process: there’s always something more you can try.

Which finally brings me to this article: I’m going to walk through the different explorations I wrote then (and a couple I’ve added in the last week) to make an LLM train _fairly_ quickly **without** resorting to using a library. Most of the code will be in Swift (although I’ll show a Metal implementation at the end).

By the way, **I will not be explaining how a neural network or an LLM works**. If you’re interested, Karpathy’s video [Let’s build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY) is practically the definitive guide to learning how GPT-like LLMs work and his earlier series starting with [The spelled-out intro to language modeling: building makemore](https://youtu.be/PaCmpygFfXo?si=SQmmakwYc2B3BfMv) covers plenty of introductory concepts in a 5 video series if you want a more introductory lesson. Of course, both are in Python, so please come back here when you’re ready to see how we can do things in Swift.

## llm.c

Machine learning is essentially the application of model weights to input data (called the forward pass, a.k.a. inference), then the calculation of error gradients and an update to those weights (the backward pass).

We typically package these calculations together and try to make them run as fast as possible. These packages of operations might be called: “linear tensor projection”, “matrix multiplication”, or even a series of “vector dot products” (depending on how big or small you slice the units of work). It’s ultimately a loop that performs `z += x * y` a _lot_ of times.

Since these matrix multiplications represent so much of the work in machine learning, I’m going to focus on the code that does this. I will be updating the rest of the implementation as I go, but only using the same improvements I’m showing to matrix multiplication.

Let’s start by looking at the `matmul_forward` from llm.c which is the core matrix multiplication used on the forward pass. It iterates over the input (`inp`), multiplies by model weights (`weight`), and adds the result to the running total (`val`).

```c
void matmul_forward(float* out, const float* inp, const float* weight, const float* bias, int B, int T, int C, int OC) {
    for (int b = 0; b < B; b++) {
        for (int t = 0; t < T; t++) {
            int bt = b * T + t;
            for (int o = 0; o < OC; o++) {
                float val = (bias != NULL) ? bias[o] : 0.0f;
                for (int i = 0; i < C; i++) {
                    val += inp[bt * C + i] * weight[o*C + i];
                }
                out[bt * OC + o] = val;
            }
        }
    }
}
```

The four layers of loops add some visual complexity but in reality, that `val += inp[bt * C + i] * weight[o*C + i];` line is the heart of a neural network. Like I said: `z += x * y` a _lot_.

How much?

The `val` line contains 2 floating point operations but Karpathy says the number of floating point operations in a full training iteration should be roughly `6 x N x D` where `N` is the number of weights in the model (124,439,808 in our case) and `D` is `B * T = 4 * 64 = 256` for our app. So we’re talking about 6 x 124,439,808 x 256 ≈ 1.911×10¹¹ ≈ 0.2 trillion floating point operations per training iteration.

So it’s got to run quick.

| Model | Tokens/s | Training iterations/s |
|---|---|---|
| llm.c | 0.92 | 0.174 |

The plain C code runs easily in a Swift Package. I’ve fixed the C implementation to always run at `-O3` optimization level (regardless of Xcode settings). Even at this optimization level, the C implementation manages just one training iteration every 7 seconds and inference at less than 1 token per second. A wonderful proof of concept but 10 times slower than would ever be useful.

## Basic Swift

I’ve tried my best to keep the basic Swift version as true to the C version as possible:

```swift
static func matmul_forward(out: inout [Float], inp: [Float], weight: [Float], bias: [Float]?, B: Int, T: Int, C: Int, OC: Int) {
    for b in 0..<B {
        for t in 0..<T {
            let bt = b * T + t
            for o in 0..<OC {
                var value = bias?[o] ?? 0
                for i in 0..<C {
                    value += inp[bt * C + i] * weight[o * C + i]
                }
                out[bt * OC + o] = value
            }
        }
    }
}
```

Since the C code is inherently “unsafe”, I went ahead and gave the Swift code the same advantage by setting it to run with `-remove-runtime-asserts` (removing the runtime checking on array indices) and made sure to always run the app in “Release” configuration. So the Swift and C implementations should be fairly equivalent, right?

> **Don’t run in Debug.** I will only be quoting Release configuration numbers. While I have run _sections_ of this in Debug, I’ve never waited around for a full 20 iteration training run in Debug. I usually keep the Scheme in Xcode set to “Release” – even during debugging.

If you read the backstory, I’ve already mentioned: this was “extremely slow”.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| Basic Swift | 0.054 | 0.014 | 7.3% |

The Swift code is between 15 and 20 times slower. That’s an LLM producing 1 token every 19 seconds. Running 20 training iterations on this engine takes nearly 30 minutes. What on Earth is going on?

> This performance represents about 2.8 Gflop/s. In 1999 [Apple ran ads for the PowerMax G4 claiming its 1 Gflop/s capability made it a weapon in the eyes of the US military](https://www.youtube.com/watch?v=OoxvLq0dFvw). Now 2.8 Gflop/s is completely unacceptable.

## Span, Egg and Span

Inspecting in Instruments, by far the biggest performance cost in the previous run is `_ArrayBuffer.beginCOWMutation()`. Swift thinks someone else could be using our `Array`s and even though they are unique (so we’re not getting array copies), the uniqueness checks alone are our biggest overhead.

> **Huh?** Sometimes you run into issues that might just be a bug. This might be one of them. When I first worked on this code in 2024, my memory is that this wasn’t a problem. I don’t know if there’s been a regression or a safety hole was covered over leading to `_ArrayBuffer.beginCOWMutation()` clogging up performance. This problem also moves around when I disable function inlining with `inline(none)` so it feels like the optimizer is just not able to do its job properly.

In any case, we can’t use `Array` and get the performance we need. Fortunately, Swift 6.2 gives us a reliable fix with basically zero overhead: `MutableSpan`.

```swift
static func matmul_forward(out: inout [Float], inp: [Float], weight: [Float], bias: [Float]?, B: Int, T: Int, C: Int, OC: Int) {
    var out = out.mutableSpan
    for b in 0..<B {
        for t in 0..<T {
            let bt = b * T + t
            for o in 0..<OC {
                var value = bias?[o] ?? 0
                for i in 0..<C {
                    value += inp[bt * C + i] * weight[o * C + i]
                }
                out[bt * OC + o] = value
            }
        }
    }
}
```

All I’ve added is the `var out = out.mutableSpan` line at the top, shadowing `out` with its own `mutableSpan`. I’ve also applied the same pattern throughout the file.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| Basic Swift | 0.054 | 0.014 | 7.3% |
| Basic Swift + mutableSpan | 0.056 | 0.042 | 24.0% |

Curiously, while this change didn’t have much impact on the forward pass, it did make the training iterations (forward + backward + update) more than 3 times faster.

## Chill vibes

But we need to turn our attention to why the forward pass is slow. Instruments confirms what we already know: the hottest line on the forward pass is the center of our loop `value += inp[bt * C + i] * weight[o * C + i]`.

It’s time to face a hard truth: C has some compiler optimization flags that Swift doesn’t have. In this specific case, C has `-ffast-math` which allows C to use fused-multiply-addition (FMA) commands which perform a floating-point multiply and addition in a single command and generally doesn’t worry too much about precise correctness.

```asm
+0xa34   fmadd               s0, s17, s16, s0
+0xa38   ldr                 s17, [x20, #0x4]
+0xa3c   fmadd               s7, s17, s16, s7
+0xa40   ldr                 s17, [x21, #0x4]
+0xa44   fmadd               s4, s17, s16, s4
+0xa48   ldr                 s17, [x22, #0x4]
+0xa4c   fmadd               s6, s17, s16, s6
+0xa50   ldr                 s17, [x23, #0x4]
+0xa54   fmadd               s1, s17, s16, s1
+0xa58   ldr                 s17, [x24, #0x4]
+0xa5c   fmadd               s2, s17, s16, s2
+0xa60   ldr                 s17, [x25, #0x4]
+0xa64   fmadd               s3, s17, s16, s3
+0xa68   ldr                 s17, [x26, #0x4]
+0xa6c   fmadd               s5, s17, s16, s5
```

The C inner loop is mostly just 8 unrolled applications of `fmadd` (the fused-multiply-add instruction).

> **Fun fact**: we live in the future, so if things like assembly language don’t make sense to you, you can drop them into your favorite LLM and it will translate it for you.

We don’t have `-ffast-math` in Swift, so instead we get separate multiplies and adds.

```asm
+0x164   fmul.4s             v1, v1, v5
+0x168   mov                 s5, v1[3]
+0x16c   mov                 s17, v1[2]
+0x170   mov                 s18, v1[1]
+0x174   fmul.4s             v2, v2, v6
+0x178   mov                 s6, v2[3]

/*...*/

+0x1d0   fadd                s0, s0, s7
+0x1d4   fadd                s0, s0, s4
+0x1d8   fadd                s0, s0, s24
+0x1dc   fadd                s0, s0, s23
+0x1e0   fadd                s0, s0, s16
```

Swift is trying to do a 4x loop unroll – that `fmul.4s` is a SIMD operation for performing 4 multiplies – but all those `mov` instructions and the separate additions at the end are hurting us.

We need to use fused-multiply-add, like C is using.

Fortunately, we have [Swift-Numerics](https://github.com/apple/swift-numerics) which offers `Relaxed` for our own version of fast math. Like the “Don’t panic” on the Hitchhiker’s Guide to the Galaxy, I’m sure the word “Relax” is just here to make us all calmer and enjoy chill vibes. Or it lets us relax the rules around rounding results so FMA is possible.

All of our `a += b * c` and `x = y + z` operations can be improved with `Relaxed.multiplyAdd` and `Relaxed.sum` but I will specifically avoid applying these functions to the `gelu_backward` function since the C implementation explicitly disables `-ffast-math` around that function.

```swift
static func matmul_forward(out: inout [Float], inp: [Float], weight: [Float], bias: [Float]?, B: Int, T: Int, C: Int, OC: Int) {
    var out = out.mutableSpan
    for b in 0..<B {
        for t in 0..<T {
            let bt = b * T + t
            for o in 0..<OC {
                var val = bias?[o] ?? 0
                for i in 0..<C {
                    val = Relaxed.multiplyAdd(inp[bt * C + i], weight[o * C + i], val)
                }
                out[bt * OC + o] = val
            }
        }
    }
}
```

The one change is there in the middle: `val = Relaxed.multiplyAdd(inp[bt * C + i], weight[o * C + i], val)`. Not as pretty to read but let’s see the performance.

Now our assembly looks like this:

```asm
+0x178   fmla.4s             v1, v16, v4
+0x17c   fmla.4s             v0, v17, v5
+0x180   fmla.4s             v2, v18, v6
+0x184   fmla.4s             v3, v19, v7
+0x188   add                 x6, x6, #0x40
+0x18c   add                 x30, x30, #0x40
+0x190   subs                x13, x13, #0x10
+0x194   b.ne                "specialized static LLMBasicSwift.matmul_forward(out:inp:weight:bias:B:T:C:OC:)+0x168"
+0x198   fadd.4s             v0, v0, v1
+0x19c   fadd.4s             v0, v2, v0
+0x1a0   fadd.4s             v0, v3, v0
+0x1a4   faddp.4s            v0, v0, v0
+0x1a8   faddp.2s            s0, v0
```

Interestingly, Swift is choosing the SIMD vectorized version of `fmadd` (`fmla`) but the premise is the same.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| Basic Swift | 0.054 | 0.014 | 7.3% |
| Basic Swift + mutableSpan | 0.056 | 0.042 | 24.0% |
| Basic Swift + mutableSpan + Relaxed | 0.533 | 0.148 | 85.1% |

That’s a nearly 10x speed increase in tokens per second. But our training performance remains 15% slower than C. How can we close the final gap?

## They see me rollin'

Time to admit something: I’ve been showing the “naive” version of matrix multiplication from C. The real C function is a little uglier as it strides over the outer loop by 8 steps at a time, hoping the compiler will unroll the innermost loop. And C’s `-O3` obliges by delivering 8x loop unrolling.

```c
for (int obt = 0; obt < B * T; obt += LOOP_UNROLL) {
    for (int o = 0; o < OC; o++) {
        float result[LOOP_UNROLL];
        for (int ibt = 0; ibt < LOOP_UNROLL; ibt++) {
            result[ibt] = (bias != NULL) ? bias[o] : 0.0f;
        }
        for (int i = 0; i < C; i++) {
            float w = weight[i + o * C];
            for (int ibt = 0; ibt < LOOP_UNROLL; ibt++) {
                int bt = obt + ibt;
                result[ibt] += inp[bt * C + i] * w;
            }
        }
        for (int ibt = 0; ibt < LOOP_UNROLL; ibt++) {
            int bt = obt + ibt;
            out[bt * OC + o] = result[ibt];
        }
    }
}
```

It might not seem obvious but the critical line here in the C implementation is the `float result[LOOP_UNROLL];` buffer to store 8 result values.

Previously we simply couldn’t do this in Swift. Allocating an `Array<Float>` in the loop was simply too high a cost. In my 2024 implementation, all I could do was manually unroll the loop 8 times (something that’s fairly hideous to read).

However, Swift 6.2 has given us another useful feature here: `InlineArray` which finally matches C stack allocated arrays.

```swift
for obt in stride(from: 0, to: BT, by: LOOP_UNROLL) {
    for o in 0..<OC {
        var result = InlineArray<8, Float>(repeating: bias?[o] ?? 0)
        let bt = inp.span.extracting(droppingFirst: obt * C)
        let w = weight.span.extracting(droppingFirst: o * C)

        for i in 0..<C {
            for r in result.indices {
                result[r] = Relaxed.multiplyAdd(bt[r * C + i], w[i], result[r])
            }
        }
      
        for r in result.indices {
            out[(obt + r) * OC + o] = result[r]
        }
    }
}
```

The assembly is just the same `fmla.4s` and `fadd.4s` instructions as the last example but more of them so there are slightly fewer branches and other overheads. Importantly: we’re now as similar as we can be to the C implementation.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| Basic Swift + mutableSpan + Relaxed | 0.533 | 0.148 | 85.1% |
| Fast Swift | 0.918 | 0.189 | 106.6% |

C and Swift are essentially the same speed for inference and Swift is now slightly faster at training.

While Swift is faster here, I’m sure you could shake a few more flags at the C compiler and get it to spit out SIMD instructions and C would jump ahead again. The key point is that the two are now roughly equivalent.

## Multi-threaded

The llm.c code contains many `#pragma` annotations like `#pragma omp parallel for` ahead of loops.

While it doesn’t run in the regular clang-compiled output used by the Swift package manager, these annotations are for OpenMP (Open Multi-Processing). OpenMP usually requires a modified C compiler but that’s how the llm.c code is intended to be run.

This is where I think Swift finally loses to C in terms of readability. Not only is there no easy way to tag a loop for parallelism but there’s no Swift 6 safe way to slice an Array and concurrently work on the separate slices. Approaches like `MutableSpan` will complain that you’re concurrently accessing variables (even if they’re made from separate slices).

**Why not Swift concurrency?** I did try `TaskGroup`. It is about the same speed (despite anecdotes claiming it would be slower). But it requires the `out.withUnsafeMutableBufferPointer` parameter escape its closure (theoretical safety violation) and offers no benefits.

Which means that all our mutable arrays will need to resort to using `withUnsafeMutableBufferPointer` and `@unchecked Sendable` wrappers so the compiler doesn’t complain about what we’re trying to do.

Our concurrency of choice will be `DispatchQueue.concurrentPerform`. This is important because its closure is not marked as `@escaping` so we can pass our immutable arrays as `Span` without incurring copying, reference count checks or other overhead.

```swift
let tileCount = BT / LOOP_UNROLL
let workerCount = max(1, ProcessInfo.processInfo.activeProcessorCount)
let chunkSize = max(1, (tileCount + workerCount - 1) / workerCount)
let chunkCount = (tileCount + chunkSize - 1) / chunkSize
let bias = bias?.span
let inp = inp.span
let weight = weight.span

out.withUnsafeMutableBufferPointer { outBuffer in
    let outStorage = SendableUnsafeMutableBuffer(baseAddress: outBuffer.baseAddress!)

    DispatchQueue.concurrentPerform(iterations: chunkCount) { chunk in
        let startTile = chunk * chunkSize
        let endTile = min(tileCount, startTile + chunkSize)

        for tile in startTile..<endTile {
            let obt = tile * LOOP_UNROLL

            for o in 0..<OC {
                var result = InlineArray<8, Float>(repeating: bias?[o] ?? 0)
                let bt = inp.extracting(droppingFirst: obt * C)
                let w = weight.extracting(droppingFirst: o * C)

                for i in 0..<C {
                    for r in result.indices {
                        result[r] = Relaxed.multiplyAdd(bt[r * C + i], w[i], result[r])
                    }
                }

                for r in result.indices {
                    outStorage[(obt + r) * OC + o] = result[r]
                }
            }
        }
    }
}
```

It’s not literally the worst code ever but:

- there’s a lot of overhead calculating the tiles and chunks and shadowing with `span`
- scope and the

  scope definitely add visual clutter

This is the iteration where I think: the C code looks better. It would be a lot nicer to have a slice-and-perform-concurrently operation on `RangeReplaceableCollection` that made this look as simple as replacing the `for` loop line.

I’ve applied this pattern to the four hottest loops in the training iterations: `matmul_forward`, `matmul_backward`, `attention_forward` and `attention_backward`.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| llm.c (omp) | n/a | 0.776 | 446% |
| Fast Swift | 0.918 | 0.189 | 106.6% |
| Multithreaded Swift | 4.356 | 1.014 | 558.5% |

I didn’t run llm.c through OMP so the training performance is taken from those quoted by Karpathy on the llm.c GitHub page (we’re both running M3 Max CPUs so it should be approximately comparable).

A 5.4x improvement. Pretty good, although I have 16 cores in my CPU so a mere 5x improvement for multi-threading isn’t perfect utilization. We’re likely getting constrained by our memory traversal, now.

The biggest problem I see is that between loop unrolling, unsafe pointers, unchecked sendable wrappers and tracking the iterations for concurrent performing, the code is now so hideous it’s very unwieldy.

We can do better.

## Top-secret hacks

I think we’ve done admirably. But it’s time to accept that if we want the fastest CPU-based matrix multiplication on Macs, we’re going to need more than the basic SIMD performance optimization that `Relaxed.multiplyAdd` and the underlying `fmla.4s` instructions get us.

So… what’s the fastest CPU instruction on Apple Silicon for matrix multiplication?

That’s where we arrive at a strange position: it’s a secret.

Apple Silicon contains a unit called the AMX (Apple Matrix Coprocessor, no relation to Intel’s AMX). I’m not sure this is the official name of this unit because Apple have never officially called it anything other than “machine learning accelerators”. The only public way to access AMX instructions is through the Accelerate framework’s BLAS implementation but using a library conflicts with this article’s premise of framework-free implementations.

Fortunately, people have [reverse engineered how the AMX unit works](https://github.com/corsix/amx) so based on some of the instructions from there, let’s see if we can write a faster matrix multiplication implementation.

> I’m having fun here but it should be clear: **don’t use Apple’s AMX instructions directly. Go through the Accelerate framework** for your own apps. Apple keep this “undocumented” so they can break binary compatibility at any time. The Accelerate framework will continue to work but this code will fail. And spoilers for the next article: Apple’s implementation is about 20% faster than mine, anyway.

The core instruction we need is `AMX_MATFP`. This instruction multiplies each element in a 16 element vector by each element in another 16 element vector, producing a 16 x 16 tile which is accumulated in the output tile. Doing this 16 times with appropriate input vectors can multiply an entire 16 x 16 matrix. We need to load the inputs so we also have `AMX_LDX` and `AMX_LDY` and at the end, we emit the 16 x 16 accumulated tile using `AMX_STZ`. Along with `AMX_LDZ` (used to reset the accumulator tiles to a predefined zero tile) gives us a way to handle the inner loop of a tiled matrix multiply.

That means that this algorithm doesn’t show the whole loop: it’s just the inner loop and an outer loop is needed to prepare the data and unify the result. I’m just going to show the inner loop.

```swift
private static func amxF32_16x64(
    outTiles: UnsafeMutablePointer<Float>,
    lhsPanel: UnsafePointer<Float>,
    rhsPanels: UnsafePointer<Float>,
    innerCount: Int
) {
    zeroTileRow.withUnsafeBufferPointer { zeroBuffer in
        guard let zeroBase = zeroBuffer.baseAddress else { return }

        for tile in 0..<accumulatorCount {
            for row in 0..<tileRows {
                amx_ldz(zeroBase.amxZOperand(row: UInt32(tile + (row * accumulatorCount))))
            }
        }

        for k in 0..<innerCount {
            let lhsBase = lhsPanel + (k * tileRows)
            amx_ldx(lhsBase.amxXYOperand)
            for tile in 0..<accumulatorCount {
                let rhsBase = rhsPanels + (tile * innerCount * tileRows) + (k * tileRows)
                amx_ldy(rhsBase.amxXYOperand)
                amx_matfp(amxMatFPF32 | (UInt64(tile) << 20))
            }
        }

        for tile in 0..<accumulatorCount {
            let tileBase = outTiles + (tile * tileRows * tileRows)
            for row in 0..<tileRows {
                let rowBase = UnsafePointer<Float>(tileBase + (row * tileRows))
                amx_stz(rowBase.amxZOperand(row: UInt32(tile + (row * accumulatorCount))))
            }
        }
    }
}
```

Once again, it’s not _that_ different in shape to the `LOOP_UNROLL` implementations that I called “Fast Swift”.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| Multithreaded Swift | 4.356 | 1.014 | 558.5% |
| AMX | 5.884 | 1.678 | 958.8% |

Another 1.67 times faster on training. Tiling requires a lot of packing and scattering of data to get our row-major matrices into the required tile shape and I’m pretty sure I could be doing a better job, there. If I was more efficient with this, it would be easily over 2 times faster.

## Maximum power draw

> The Metal code in **this implementation is derived from an implementation by James Thompson** in [llm.metal](https://github.com/regrettable-username/llm.metal). However, they used a library for matrix multiplication, so I’ve written my own Metal matrix multiplication code to keep the framework-free approach going.

In the previous section, I was careful to say “the fastest _CPU_ instruction on Apple Silicon for matrix multiplication” because, of course, we also have the GPU.

What does Metal code look like for matrix multiplication? Unlike the C and Swift code, it’s in two parts: the inner kernel (which we write in Metal/C++) and the outer invocation machinery (which stays on the Swift side).

First, the inner kernel:

```cpp
kernel void matmul_forward_kernel(
    device float* out [[buffer(0)]],
    const device float* inp [[buffer(1)]],
    const device float* weight [[buffer(2)]],
    const device float* bias [[buffer(3)]],
    constant uint& BT [[buffer(4)]],
    constant uint& C [[buffer(5)]],
    constant uint& OC [[buffer(6)]],
    uint2 gid [[thread_position_in_grid]]
) {
    uint oc = gid.x;
    uint bt = gid.y;
    if (bt >= BT || oc >= OC) {
        return;
    }

    float sum = bias[oc];
    for (uint i = 0; i < C; i++) {
        sum += inp[bt * C + i] * weight[oc * C + i];
    }
    out[bt * OC + oc] = sum;
}
```

Skipping over the somewhat heavy parameter block, you can see that all this really contains is the innermost loop of the four loops in the C and Basic Swift `matmul_forward`. Instead of loops over `B`, `T`, `OC` and `C`, we just have the loop over `C` here.

Iterating over `B * T` and `OC` is handled in the outer machinery:

```swift
func matmul_forward(out: MTLBuffer, inp: MTLBuffer, weight: MTLBuffer, bias: MTLBuffer, B: Int, T: Int, C: Int, OC: Int, ctx: MetalCommandContext) {
    ctx.compute.compute2D(
        pipelines.matmulForward,
        width: OC,
        height: B * T,
        threadsPerThreadgroup: MTLSize(width: 1, height: 1, depth: 1),
        buffers: [out, inp, weight, bias],
        uints: [UInt32(B * T), UInt32(C), UInt32(OC)]
    )
    ctx.endCompute()
}
```

where I’ve implemented compute2D as a helper that looks like this:

```swift
func compute2D(
    _ pipeline: MTLComputePipelineState,
    width: Int,
    height: Int,
    threadsPerThreadgroup: MTLSize,
    buffers: [MTLBuffer],
    uints: [UInt32] = []
) {
    setComputePipelineState(pipeline)
    for (i, buf) in buffers.enumerated() {
        setBuffer(buf, offset: 0, index: i)
    }
    var uintsCopy = uints
    for i in 0..<uintsCopy.count {
        setBytes(&uintsCopy[i], length: MemoryLayout<UInt32>.stride, index: buffers.count + i)
    }
    dispatchThreads(
        MTLSize(width: width, height: height, depth: 1),
        threadsPerThreadgroup: threadsPerThreadgroup
    )
}
```

Do you remember when I said, about multi-threaded Swift: “It would be a lot nicer to have a slice-and-perform-concurrently operation”? That’s really what this is: carving up the `buffers` into a set of tiles that can be concurrently acted upon. The `width` and `height` parameters here get translated into the `gid.x` and `gid.y` parameters in the kernel code, allowing us to index into the `inp` and `weight` buffers, in an almost identical fashion to the Basic Swift code.

You can see that we’re invoking the `matmulForward` pipeline as a two dimensional set of “threads” (not CPU threads but GPU workers). If you imagine the `B` and `T` loops from the Basic Swift implementation flattened into a single `B * T` then we’re literally doing the same work, just on power-hungry GPU, not the CPU.

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| AMX | 5.884 | 1.678 | 958.8% |
| Basic Metal | 4.29 | 1.841 | 1052.0% |

It’s not a huge improvement over the AMX implementation. Training is slightly faster but inference is slower. For a power-hungry, high end GPU, it’s not much of an improvement.

As with everything else, we don’t magically get top-tier performance with the simplest, most naive approach.

Of course, adding “threading” on the GPU is much simpler than it was on the CPU. Doing nothing more than changing that `threadsPerThreadgroup` parameter to `MTLSize(width: 16, height: 16, depth: 1)` will bump our times up to

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| AMX | 5.884 | 1.678 | 958.8% |
| Basic Metal | 4.29 | 1.841 | 1052.0% |
| Threaded Metal | 6.211 | 2.431 | 1389.1% |

An easy win, if not a huge improvement.

What we really need to do is start tiling the matrix – similar to how the AMX solution worked – so we’re accessing memory in a more-local way (rather than traversing the entire long rows on each inner loop).

There are people who love writing tight kernels and tile packing and scattering, but it’s not really my strength. Here’s my best effort at a Metal tiling kernel:

```cpp
kernel void matmul_forward_kernel(
    device float* out [[buffer(0)]],
    const device float* inp [[buffer(1)]],
    const device float* weight [[buffer(2)]],
    constant uint& BT [[buffer(3)]],
    constant uint& C [[buffer(4)]],
    constant uint& OC [[buffer(5)]],
    uint2 gid [[thread_position_in_grid]],
    uint2 lid [[thread_position_in_threadgroup]]
) {
    threadgroup float inpTile[MATMUL_TILE][MATMUL_TILE];
    threadgroup float weightTile[MATMUL_TILE][MATMUL_TILE];

    uint oc = gid.x;
    uint bt = gid.y;
    bool inBounds = bt < BT && oc < OC;
    float sum = 0.0f;

    for (uint kBase = 0; kBase < C; kBase += MATMUL_TILE) {
        uint inpK = kBase + lid.x;
        uint weightK = kBase + lid.y;
        inpTile[lid.y][lid.x] = (bt < BT && inpK < C) ? inp[bt * C + inpK] : 0.0f;
        weightTile[lid.y][lid.x] = (oc < OC && weightK < C) ? weight[oc * C + weightK] : 0.0f;
        threadgroup_barrier(mem_flags::mem_threadgroup);
        for (uint k = 0; k < MATMUL_TILE; k++) {
            sum += inpTile[lid.y][k] * weightTile[k][lid.x];
        }
        threadgroup_barrier(mem_flags::mem_threadgroup);
    }

    if (inBounds) {
        out[bt * OC + oc] = sum;
    }
}
```

As we’ve seen in previous attempts to optimize: this is much harder to read but it does provide another incremental improvement.

Since this is as far as I’m going to go with it, let’s take a look at the complete table:

| Model | Tokens/s | Training iterations/s | Training versus llm.c |
|---|---|---|---|
| llm.c | 0.926 | 0.175 | 100% |
| llm.c (omp) | n/a | 0.776 | 446% |
| Basic Swift | 0.054 | 0.014 | 7.3% |
| Basic Swift + mutableSpan | 0.056 | 0.042 | 24.0% |
| Basic Swift + mutableSpan + Relaxed | 0.533 | 0.148 | 85.1% |
| Fast Swift | 0.918 | 0.189 | 106.6% |
| Multithreaded Swift | 4.356 | 1.014 | 558.5% |
| AMX | 5.884 | 1.678 | 958.8% |
| Basic Metal | 4.29 | 1.841 | 1052.0% |
| Threaded Metal | 6.211 | 2.431 | 1389.1% |
| Tiled Metal | 11.123 | 3.371 | 1926.3% |

This is around 650 Gflop/s _[Edit: yeah, sorry, this is a correction down from the 1 Tflop/s in the title]_ but even if I generously round back up to the nearest 1 significant figure, is 1 Tflop/s good? Theoretically, the GPU on my M3 Max is capable of around 15 Tflop/s. The real ceiling for this kind of task is going to be 3-5 Tflop/s (for a number of different reasons) – definitely more than the performance I’m getting out of my handwritten Metal matrix code.

There’s an interesting question here: I have a high-end GPU. On a base M-series chip, would the performance ratio between AMX unit and GPU change?

## Test harness

![CwlLlmSwift showing comparison between all engines on the TinyShakespeare training set](https://www.cocoawithlove.com/assets/blog/cwlllmswift.png)

<sub>CwlLlmSwift showing comparison between all engines on the TinyShakespeare training set</sub>

You can download the code and test harness app from [CwlLlmSwift](https://github.com/mattgallagher/CwlLlmSwift). You will also need to download the [llmc-starter-pack](https://huggingface.co/datasets/karpathy/llmc-starter-pack) used by Andrej Karpathy’s llm.c. **NOTE that cloning llmc-starter-pack correctly requires `git-xet` installed**:

```
brew install git-xet
git xet install
```

Without git set, the files in the starter pack won’t download correctly and selecting them in the app will give errors about the training file not being UInt16 weights.

**WARNING:** I’ve already recommended to always run the app in “Release” configuration but even in “Release”, the 20 iteration training comparison for “Basic Swift” takes around 30 minutes to run (you can see the “Total” times in that screenshot, above). Most of the time you’ll want to disable the “Basic Swift” engine and just view the others.

When you start the app for the first time, it’ll show an open dialog but you’ll want to hit the “New document” button. This will show a blank document that will require you to select the following documents from the llmc-starter-pack:

- gpt2_124M.bin (checkpoint)
- tiny_shakespeare_train.bin (training data)
- tiny_shakespeare_val.bin (validation data)
- gpt2_tokenizer.bin (tokenizer)

Then hit the “Create” button to create the dataset. Once the dataset is created, you can run training, inference or comparisons and save the dataset as a document.

To be clear: the actual GPT-2 style LLM is pretty mediocre (it is only a 124-million-parameter model, where most LLMs start in the billions of parameters). Here’s an example of the model at the gpt2_124M.bin checkpoint (before running any post-training):

> **Prompt:** The quick brown fox   
>  **Generation:** would register the decision to slowdown his steps as he held out his right paw to hold up place. As Cas mornarye yelped as the fox clutched at his paw his temper ground up. “You sure you’re not scared of birds?”

And after 500 iterations of post-training on Shakespeare:

> **Prompt:** The quick brown fox  
>  **Generation:** charged,  
>  Barking as he did,  
>  To fight withanna in his bosom,  
>  On one occasion dying:  
>  No fault is his life, for there blood being out. ’tis I;  
>  I did mean death, though it be by the water.

Both examples look okay from a distance but are somewhat incoherent in the details. Not exactly AGI.

For comparison, here’s what I get out of `LanguageModelSession`, Apple’s Foundation model built into iOS/macOS 26, where the only “training” needed is the prompt you give it:

> **Prompt:** Turn the prompt “The quick brown fox” into a few lines of verse in Shakespearean language and meter.  
>  **Generation:** Upon the heath, a swift fox doth roam,  
>  His coat of brown, like autumn’s golden hue,  
>  With nimble steps, he darts through the foam,  
>  A creature swift, both bold and true.

I don’t think this model has really nailed iambic pentameter but it’s at least coherent. If you need a quick and readily available LLM on macOS, use Apple’s Foundation model. But the point of this series isn’t to show how to create the best model, it’s merely to explore how to run a model and perform post-training.

## Conclusion

> This article was about looking at how to optimize code and gaining appreciation for the work that needs to go into optimizing the matrix multiplications in machine learning libraries. **None of this code should be considered a good choice for production**. In the next article, I’ll look at BLAS, BNNS, CoreML, MPSGraph and other high performance libraries built into macOS. These libraries are all either more efficient or more performant than the options I’ve shown here.

We took a basic Swift implementation of matrix multiplication and made it 232 times faster, taking it from 2.8 Gflop/s to 650 Gflop/s. In the process, we’ve seen the scaling capability from unoptimized code, slightly improved code, to SIMD optimized code, to multithreaded code, to running on special units, to GPU compute shaders.

The first 72 times increase occurred due to the basic Swift optimizations you should consider for any algorithm:

- copy-on-write/reference-check overhead (Swift should have applied this automatically; it is maybe just a bug)
- Use some SIMD optimized fused-multiply-add instructions in Swift (by “relaxing” constraints using the Numerics library)
- Restructured loops so the traversal is more efficient and SIMD pipelining works better
- Parallelize using `DispatchQueue.concurrentPerform`

As always, high performance Swift has plenty of curve-balls to throw but it’s always possible to get Swift as fast as C. This time, Swift ended up faster due to Swift choosing slightly better SIMD instructions (although I’m sure there’s a way to get C to use the same SIMD versions of FMA for the same performance).

The question is never whether Swift can be fast, but rather: will Swift look better when you get there? I think Swift held up well until the multi-threaded implementation. Using `withUnsafeMutableBuffer` ruins the aesthetics of any function. I wish Swift had functions for performing mutations over subranges of an array to do this elegantly, safely and with good performance.

Moving beyond typical Swift optimization, using AMX instructions got us another 70% faster using operations on Apple Silicon designed for larger matrix operations. The final boost came from moving to the graphics card. In both these cases, you’d get much better results from a developer skilled in tiled matrix operations. My efforts were “okay” but I know that performance could be 30% better if I really knew what I was doing.

But 382 times faster still isn’t fast enough. Even this example gave us **less than 12 tokens per second** – a speed which might be barely passable in some cases but for a model this small is laughably slow.

Clearly, we’ve got further to go.

Apple have lots of other frameworks for training neural networks and the final implementation in this series will knock out more than 20 training iterations before most of the implementations in this article have spat out their first.
