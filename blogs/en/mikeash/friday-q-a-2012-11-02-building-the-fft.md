---
title: 'Friday Q&A 2012-11-02: Building the FFT'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-11-02-building-the-fft.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eaa51e2c5d3afa36'
translated: false
---

> 原文：[Friday Q&A 2012-11-02: Building the FFT](https://www.mikeash.com/pyblog/friday-qa-2012-11-02-building-the-fft.html)　·　mikeash.com Friday Q&A

Posted at 2012-11-02 14:29 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-11-09: dyld: Dynamic Linking On OS X](https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html)  
Previous article: [Friday Q&A 2012-10-26: Fourier Transforms and FFTs](https://www.mikeash.com/pyblog/friday-qa-2012-10-26-fourier-transforms-and-ffts.html)  
Tags: [audio](https://www.mikeash.com/pyblog/?tag=audio) [fft](https://www.mikeash.com/pyblog/?tag=fft) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa) [guest](https://www.mikeash.com/pyblog/?tag=guest)

Friday Q&A 2012-11-02: Building the FFT

by [Chris Liscio](http://supermegaultragroovy.com)

In this installment, I'll show you how we get from point A to point B. Specifically, I'll talk a bit about the magic behind the Fast Fourier Transform.

**A bit of math (British localization: Some maths)**  
Fourier Transforms have some interesting mathematical properties. Most importantly, Fourier Transforms are a _linear_ operation. That is, if we use  to denote the Fourier Transform of :

So whether you scale or add two signals in the time or frequency domain is up to you. That's pretty handy when you're working on signal processing code. But I digress.

In addition to the above, there are some more interesting properties relating the time and frequency domain representations of a function. We'll use  to relate the time and frequency domain representations.

Don't focus too much on the individual relations themselves. The main point that I'm trying to get across is that we can manipulate the Fourier Transform and the signal in meaningful ways, and relate those changes between domains.

**The Discrete Fourier Transform**  
Before we continue, I'd like to make a clarification of sorts. The mathematical properties above are using terminology specific to Fourier Transforms of continuous functions defined over infinite time and frequency.

Obviously we're working in a digital world, and we don't have the luxury of continuous signals to work with. In software, we're dealing with sampled data, which is where the Discrete Fourier Transform comes in.

This is basically what Mike already gave you in code form in his [last post on the topic](https://www.mikeash.com/pyblog/friday-qa-2012-10-26-fourier-transforms-and-ffts.html), and I encourage you to take another look at his code to understand how it relates to this equation.

What's important is that you understand the Discrete Fourier Transform and Continuous Fourier Transforms are closely related, and have almost exactly the same mathematical properties as described above. For what we're discussing, you can safely ignore the "almost" part, and look to [Wikipedia's definition](http://en.wikipedia.org/wiki/Discrete_Fourier_transform) for more discussion.

**The Danielson-Lanczos lemma**  
Using a combination of the mathematical properties of the Fourier Transform above, Danielson and Lanczos discovered that you can rewrite a Discrete Fourier Transform of length N as a sum of two Discrete Fourier Transforms of length N/2: one from the even-numbered and one from the odd-numbered points of input.

This is their proof:

Here, , and  and  are the even and odd terms of , respectively.

Again, it's not important to totally understand the above, or how they got from A to B. This is where I wave my hands and defer to the fact that the mathematical properties of the Discrete Fourier Transform have been used in the derivation.

**The Fast Fourier Transform**  
The discovery by Danielson and Lanczos, combined with the fact that it can be applied recursively, is the basis of the Fast Fourier Transform. Breaking the problem down one more step, we will end up with a combination of , , , and .

If we stick with power-of-two inputs to the Fourier Transform, we will guarantee that the problem continues to decompose until we reach a fourier transform on one element. And, guess what? That's just a copy of the input value:

There is a way to derive the value of , but I'm choosing to wave my hands again.

Instead, I'm going to let recursion do the work for us. I vote for this option, to keep this post from exploding out of control. Also, get your hands on a copy of [Numerical Recipes](http://www.nr.com) to really go deep.

**(Fairly) Straightforward Implementation**  
I put together a compact implementation that demonstrates how this all works. It is based on the first optimization, because I think it's a good balance of readability with just a hint of cleverness. (I started out based on [this resource](http://en.literateprograms.org/Cooley-Tukey_FFT_algorithm_%28C%29), but massaged the implementation for clarity, and to closely match my math above.)

```
    static complex double *FFT_recurse( complex double *x, int N, int skip ) {
        complex double *X = (complex double*)malloc( sizeof(complex double) * N );
        complex double *O, *E;

        // We've hit the scalar case, and copy the input to the output.
        if ( N == 1 ) {
            X[0] = x[0];
            return X;
        }

        E = FFT_recurse( x, N/2, skip * 2 );
        O = FFT_recurse( x + skip, N/2, skip * 2 );

        for ( int k = 0; k < N / 2; k++ ) {
            O[k] = ( cexp( 2.0 * I * M_PI * k / N ) * O[k] );
        }

        // While E[k] and O[k] are of length N/2, and X[k] is of length N, E[k] and
        // O[k] are periodic in k with length N/2. See p.609 of Numerical Recipes
        // in C (3rd Ed, 2007). [CL]
        for ( int k = 0; k < N / 2; k++ ) {
            X[k] = E[k] + O[k];
            X[k + N/2] = E[k] + O[k];
        }

        free( O );
        free( E );

        return X;
    }

    complex double *FFT( complex double *x, int N ) {
        return FFT_recurse( x, N, 1 );
    }
```

It's really not that complicated, but the improvement in performance is immense. I put together some driver code and [tossed it all up on my github account](https://github.com/liscio/fft). Some simple timings revealed that a straightforward "math definition" of the algorithm took approximately 12.1s, and the FFT implementation above took a mere 0.1s. More than a 100x speed increase, and that's with a whole bunch of `malloc()`s and `free()`s strewn about!

**In closing**  
I hope that this explanation was somewhat helpful in demystifying the Fast Fourier Transform and how it works. It's one of many examples of algorithms that exploit mathematics in order to gain an order-of-magnitude speedup.

Oh, and in case Mike didn't make it clear, you should _never implement this yourself_. Use the vDSP routines in Accelerate.framework!

Apple's performance team continues to push the limits of their FFT implementation year after year on all platforms. A combination of mathematicians, physicists, engineers, scientists, and assembly language wizards are working hard to ensure that Accelerate.framework is always running as fast, and power-efficient as possible.

I'm of the opinion that Apple's performance team is largely responsible for what makes the "cool stuff" on the iPhone possible. Think about live audio effects in Garage Band, video effects in iMovie, the processing in iPhoto, and so forth. All of that stuff is depending on Accelerate.framework in some capacity.

The next time you visit WWDC, make some time to stop by their lab with any performance questions you may have that relate to Accelerate.framework. They're really nice folks, and astoundingly smart, too!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-11-02-building-the-fft.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
