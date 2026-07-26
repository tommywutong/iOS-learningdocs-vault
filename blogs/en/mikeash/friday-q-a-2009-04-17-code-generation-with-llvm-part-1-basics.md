---
title: 'Friday Q&A 2009-04-17: Code Generation with LLVM, Part 1: Basics'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4ce2e14e6b6580a3'
translated: false
---

> 原文：[Friday Q&A 2009-04-17: Code Generation with LLVM, Part 1: Basics](https://www.mikeash.com/pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)　·　mikeash.com Friday Q&A

Posted at 2009-04-17 11:07 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2009-04-24: Code Generation with LLVM, Part 2: Fast Objective-C Forwarding](https://www.mikeash.com/pyblog/friday-qa-2009-04-24-code-generation-with-llvm-part-2-fast-objective-c-forwarding.html)  
Previous article: [Friday Q&A 2009-04-10: Multithreaded Optimization in ChemicalBurn](https://www.mikeash.com/pyblog/friday-qa-2009-04-10-multithreaded-optimization-in-chemicalburn.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [llvm](https://www.mikeash.com/pyblog/?tag=llvm)

Friday Q&A 2009-04-17: Code Generation with LLVM, Part 1: Basics

by [Mike Ash](https://www.mikeash.com/)

**What is LLVM?**  
 About a month ago [I talked about the Clang Static Analyzer](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html), a really handy code analyzer which can point out all kinds of errors in your programs. The static analyzer is actually an offshoot of LLVM.

[LLVM](http://llvm.org/) stands for Low Level Virtual Machine. As far as what this means, it's basically a compiler toolkit designed to be usable for just-in-time compilation. That makes it sound smaller than it really is, though. It's a huge project which provides a wealth of features in many compiler-related areas. For more information about everything it can do, click the magic link.

Among the many things LLVM is capable of, it allows you to construct code at runtime, compile it to native code, and then get a function pointer that you can call right from your own code. This means that you can build custom code on demand and get full native speed from it. Very cool!

**Building Code**  
 This week I'm going to walk through how to use LLVM to build two basic functions. The first function will just perform a multiply and add on its arguments, and the second one, a bit more complex, will be a recursive greatest common denominator function. Of course it would be a lot easier to just write these functions in plain old C, but the point is to illustrate the technique, not actually build something useful just yet.

I'll post code snippets as I go, but if you'd like to see the entire test program, you can [get it here](https://www.mikeash.com/pyblog/llvmtest.cpp). To use it, you will of course have to install LLVM. Instructions for that can be found on the LLVM site, but it's pretty much like any other UNIX package.

This code is mainly cobbled together from the [LLVM tutorials](http://llvm.org/docs/tutorial/). However, they're a bit incomplete when it comes to the basics (the "simple" tutorial shows how to build the functions but not how to compile them) and occasionally don't quite work, so I thought it would be useful to present a complete example.

The first thing to do is to create a new `Module`. This is basically a container that functions can be put into. This little function creates a new `Module`, generates the two functions, and then returns it so that we can use it.

```
    Module* makeLLVMModule()
    {
        // Module Construction
        Module* mod = new Module("test");
        
        BuildMulAdd(mod);
        BuildGCD(mod);
        
        return mod;
    }
```

There's really nothing interesting going on here. Those build functions are where the interesting work happens.

Let's look at `BuildMulAdd`. The purpose of this function is just to compute `x*y+z`, where those variables are the three parameters to the function. The first thing it does is create a new `Function` object to work with:

```
    void BuildMulAdd(Module *mod)
    {
        Constant* c = mod->getOrInsertFunction("mul_add",
        /*ret type*/                           IntegerType::get(32),
        /*args*/                               IntegerType::get(32),
                                               IntegerType::get(32),
                                               IntegerType::get(32),
        /*varargs terminated with null*/       NULL);
        
        Function* mul_add = cast(c);
        mul_add->setCallingConv(CallingConv::C);
```

The first line creates the object, which for some reason is typed `Constant`. (My understanding of the system is not quite at 100% yet.) You give it a name, and the return and argument types, and it creates the object. We cast it to the right type, and set up the calling conventions. So far, so good.

The next thing to do is extract the individual arguments so that we can use them when creating the function body. While we're at it, we'll also give them names. LLVM works by building code in what's called the LLVM intermediate representation, which acts as a kind of high level, portable assembly language. That IR is then translated into machine code when required. These names are used when building the IR to make it easier to read, but are not required. Here's how to set up the arguments:

```
        Function::arg_iterator args = mul_add->arg_begin();
        Value* x = args++;
        x->setName("x");
        Value* y = args++;
        y->setName("y");
        Value* z = args++;
        z->setName("z");
```

The next thing to do is to set up a basic block. LLVM code is organized in terms of basic blocks. A basic block is just a block of code which has no branches. In this case, since the function has no branches anyway, a single basic block takes care of the entire function:

```
        BasicBlock* block = BasicBlock::Create("entry", mul_add);
```

The next thing is to create an `IRBuilder`. This is an object that helps with building the intermediate representation. It's basically a helper object. It's possible to create things more directly, but `IRBuilder` makes building code much easier:

```
        IRBuilder<> builder(block);
```

The next thing is to actually create the instructions for the function body. This is nice and simple, since it's just a single multiply followed by a single add:

```
        Value* tmp = builder.CreateBinOp(Instruction::Mul,
                                         x, y, "tmp");
        Value* tmp2 = builder.CreateBinOp(Instruction::Add,
                                          tmp, z, "tmp2");
```

Like the arguments, the intermediate values also get names that will show up in the IR code. `tmp2` contains the desired result, so now we return it:

```
        builder.CreateRet(tmp2);
    }
```

And that's it! Easy enough. Of course we can't actually execute the thing yet. But before we get to that, let's look at the `BuildGCD` function.

**Greatest Common Denominator**  
 The goal is to build a `gcd` function using the standard recursive algorithm, like so:

```
    int gcd(int x, int y)
    {
        if(x == y)
            return x;
        else if(x < y)
            return gcd(x, y - x);
        else
            return gcd(x - y, y);
    }
```

The initial setup to the function is virtually identical:

```
    void BuildGCD(Module *mod)
    {
        Constant *c = mod->getOrInsertFunction("gcd",
                                               IntegerType::get(32),
                                               IntegerType::get(32),
                                               IntegerType::get(32),
                                               NULL);
        Function *gcd = cast<Function>(c);
        
        Function::arg_iterator args = gcd->arg_begin();
        Value *x = args++;
        x->setName("x");
        Value *y = args++;
        y->setName("y");
```

Next we'll set up the basic blocks needed by the function. In this case there are five needed. We need one entry block, which will contain the first `if`. We need a block to execute the `return` for the case where the `if` is true. A third block contains the second `if` The forth and fifth blocks handle the true and false branches of that:

```
        BasicBlock *entry = BasicBlock::Create("entry", gcd);
        BasicBlock *ret = BasicBlock::Create("return", gcd);
        BasicBlock *condFalse = BasicBlock::Create("condFalse", gcd);
        BasicBlock *condTrue = BasicBlock::Create("condTrue", gcd);
        BasicBlock *condFalse2 = BasicBlock::Create("condTrue", gcd);
```

Next we'll build code for these blocks. Since it's all relatively straightforward, and the LLVM documentation and tutorials will explain it better than I can, I'm just going to gloss over it and dump it out here:

```
        IRBuilder<> builder(entry);
        Value *xeqy = builder.CreateICmpEQ(x, y, "tmp");
        builder.CreateCondBr(xeqy, ret, condFalse);
        
        builder.SetInsertPoint(ret);
        builder.CreateRet(x);
        
        builder.SetInsertPoint(condFalse);
        Value *xlty = builder.CreateICmpULT(x, y, "tmp");
        builder.CreateCondBr(xlty, condTrue, condFalse2);
        
        builder.SetInsertPoint(condTrue);
        Value *yminusx = builder.CreateSub(y, x, "tmp");
        std::vector<Value *> args1;
        args1.push_back(x);
        args1.push_back(yminusx);
        Value *recurCall1 = builder.CreateCall(gcd, args1.begin(), args1.end(), "tmp");
        builder.CreateRet(recurCall1);
        
        builder.SetInsertPoint(condFalse2);
        Value *xminusy = builder.CreateSub(x, y, "tmp");
        std::vector<Value *> args2;
        args2.push_back(xminusy);
        args2.push_back(y);
        Value *recurCall2 = builder.CreateCall(gcd, args2.begin(), args2.end(), "tmp");
        builder.CreateRet(recurCall2);
    }
```

Notice how all of the intermediate variables are called `"tmp"`. This is not a very useful thing to do, but it does illustrate that LLVM will automatically change these names as needed to ensure that they don't conflict, which is useful. You'll be able to see this in the generated intermediate representation, which we'll get to in a bit.

That's how to build the functions, now let's see how to use them. First thing is to actually call the function to build the module, with the functions within:

```
    int main(int argc, char**argv)
    {
        Module* Mod = makeLLVMModule();
```

The next thing is to call the `verifyModule` function on the new `Module`. I'll be honest with you: I have no idea what this does, but the tutorial did it so I'm doing it too!

```
        verifyModule(*Mod, PrintMessageAction);
```

Now that the module is ready, I want to print it out. This just dumps the intermediate representation that's been built for the module. This step is not required, but is interesting and can help with debugging:

```
        PassManager PM;
        ModulePass *pmp = createPrintModulePass(&outs;());
        PM.add(pmp);
        PM.run(*Mod);
```

Now on to the really interesting stuff: compiling and running the code. This is done by using an `ExceutionEngine` object:

```
        ExecutionEngine *engine = ExecutionEngine::create(Mod);
```

Here's the really cool part. You use `getPointerToFunction` to get a function pointer from the `ExecutionEngine`. And this is a _real_ function pointer. You can call it like you would any other function. Just cast it to the right type, add parentheses and parameters, and off you go.

```
        typedef int (*MulAddFptr)(int, int, int);
        MulAddFptr fptr = (MulAddFptr)engine->getPointerToFunction(Mod->getFunction("mul_add"));
        
        typedef int (*GCDFptr)(int, int);
        GCDFptr gcd = (GCDFptr)engine->getPointerToFunction(Mod->getFunction("gcd"));
        
        fprintf(stderr, "%p: 2*3+4 = %d\n", fptr, fptr(2, 3, 4));
        fprintf(stderr, "%p: gcd(10, 25) = %d, gcd(1234, 5678) = %d\n", gcd, gcd(10, 25), gcd(1234, 5678));
```

How neat is that? That's all it takes to compile and run these functions. All that's left is cleanup:

```
        delete Mod;
        return 0;
    }
```

That's the whole program. Here's what it prints:

```
    ; ModuleID = 'test'
    
    define i32 @mul_add(i32 %x, i32 %y, i32 %z) {
    entry:
        %tmp = mul i32 %x, %y		; <i32> [#uses=1]
        %tmp2 = add i32 %tmp, %z		; <i32> [#uses=1]
        ret i32 %tmp2
    }
    
    define i32 @gcd(i32 %x, i32 %y) {
    entry:
        %tmp = icmp eq i32 %x, %y		; <i1> [#uses=1]
        br i1 %tmp, label %return, label %condFalse
    
    return:		; preds = %entry
        ret i32 %x
    
    condFalse:		; preds = %entry
        %tmp2 = icmp ult i32 %x, %y		; <i1> [#uses=1]
        br i1 %tmp2, label %condTrue, label %condTrue1
    
    condTrue:		; preds = %condFalse
        %tmp3 = sub i32 %y, %x		; <i32> [#uses=1]
        %tmp4 = call i32 @gcd(i32 %x, i32 %tmp3)		; <i32> [#uses=1]
        ret i32 %tmp4
    
    condTrue1:		; preds = %condFalse
        %tmp5 = sub i32 %x, %y		; <i32> [#uses=1]
        %tmp6 = call i32 @gcd(i32 %tmp5, i32 %y)		; <i32> [#uses=1]
        ret i32 %tmp6
    }
    0x1880010: 2*3+4 = 10
    0x1880030: gcd(10, 25) = 5, gcd(1234, 5678) = 2
```

As you can see, the intermediate representation code is nicely readable. If something is going wrong, reading it can be a good check to make sure that you're actually generating the code that you want. After it prints the intermediate representation, miracle of miracles, it prints the correct numbers too!

**Conclusion**  
 Although it's pretty pointless to build static functions using LLVM like this, it illustrates interesting techniques. Using this as a base, you can easily take these code generation functions and make them dynamic, so that they generate code in a way that you simply couldn't do from plain C. Next week, I'll show how you can use LLVM to generate Objective-C methods on the fly and actually build something almost useful from it.

That wraps up this week's edition. Remember that Friday Q&A is driven by your ideas, so send them in. Obviously I won't be able to use your idea next week, but rest assured that I save them and use them in the future. Tune in next week for the exciting conclusion, and post your comments below.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
