---
title: Exploring LLVM Bitcode interactively - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/exploring-llvm-bitcode-interactively/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0b401e973ec8a6d4'
translated: false
---

> 原文：[Exploring LLVM Bitcode interactively - Low Level Bits 🇺🇦](https://lowlevelbits.org/exploring-llvm-bitcode-interactively/)　·　Low Level Bits (Alex Denisov)

# Exploring LLVM Bitcode interactively

_Published on Feb 28, 2020_

While working on [a tool for software analysis](https://ocular.shiftleft.io), I find myself looking into the bitcode quiet often. It works OK when there is one small file, but it’s incredibly annoying when it comes to real-world projects which have tens and hundreds of files.

To simplify my life, I built a tool that converts LLVM Bitcode into the GraphML format: [llvm2graphml](https://github.com/ShiftLeftSecurity/llvm2graphml).

## What is GraphML

GraphML is an XML-based file format for storing graphs. The beautiful part is that it supported by many tools: you can use Neo4J, Cassandra, or TinkerPop to mine data or things like yEd or Gephi to visualize it.

My use-case is graph databases.

## What is Graph Database

To understand what a graph database is to think of SQLite but for property graphs. And a property graph is simply a graph where each vertex (or node) and edge may have several key-value properties.

The classical example: there is a number of people in the graph and they have some relationship, e.g.: ‘Alice -\> knows -\> Bob’, ‘Bob -\> friends-with -\> Eve’, etc. In this case, we can model a query like “Find friends of people whom Alice knows” in the form of a query language:

```groovy
graph.vertex('person').has('name', 'Alice').edge('knows').edge('friends-with')
```

Each step narrows down the search space:

- from a graph get all the vertices labeled ‘person’
- among those select the ones that have the property ’name’ with the value ‘Alice’
- from the vertices select nodes through edges labeled ‘knows’
- and from what’s left pick all the nodes reachable through the edges labeled ‘friends-with’

_Note: this is an imaginary, simplified query language, but you’ve got the idea._

## llvm2graphml

Let me walk you through an example of how to use `llvm2graphml`. To follow along you need to install `llvm2graphml` itself ([prebuilt packages](https://github.com/ShiftLeftSecurity/llvm2graphml/releases) available for macOS and Ubuntu) and [Gremlin Console](https://www.apache.org/dyn/closer.lua/tinkerpop/3.4.6/apache-tinkerpop-gremlin-console-3.4.6-bin.zip) from [Apache TinkerPop](http://tinkerpop.apache.org) project.

There are essentially three steps:

1. Create `main.ll` file with the following content:

```ll
; main.ll
define i32 @increment(i32 %x) {
  %result = add i32 %x, 1
  ret i32 %result
}
```

2. Run `llvm2graphml` to emit the GraphML file:

```sh
> llvm2graphml --output-dir=/tmp main.ll
[info] More details: /tmp/llvm2graphml-38dfea.log
[info] Loading main.ll
[info] Saved result into /tmp/llvm.graphml.xml
[info] Shutting down
```

3. Create the database from the GraphML file

Start console:

```sh
> gremlin-console/bin/gremlin.sh

         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
plugin activated: tinkerpop.server
plugin activated: tinkerpop.utilities
plugin activated: tinkerpop.tinkergraph
gremlin>
```

Create the database:

```groovy
gremlin> graph = TinkerGraph.open()
gremlin> g = graph.traversal()
gremlin> g.io("/tmp/llvm.graphml.xml").read()
gremlin> g
==>graphtraversalsource[tinkergraph[vertices:12 edges:27], standard]
```

Now go and run some queries!

## Example queries

List all modules:

```groovy
gremlin> g.V().hasLabel('module').valueMap().unfold()
==>moduleIdentifier=[main.ll]
```

List all functions:

```groovy
gremlin> g.V().hasLabel('function').valueMap().unfold()
==>argSize=[1]
==>basicBlockCount=[1]
==>name=[increment]
==>isDeclaration=[false]
==>isVarArg=[false]
==>isIntrinsic=[false]
==>numOperands=[0]
==>instructionCount=[2]
```

Count all the instructions:

```groovy
gremlin> g.V().hasLabel('instruction').groupCount().by('opcode').unfold()
==>ret=1
==>add=1
```

Explore the types:

```groovy
gremlin> g.V().hasLabel('type').valueMap('typeID').unfold()
==>typeID=[label]
==>typeID=[pointer]
==>typeID=[function]
==>typeID=[integer]
==>typeID=[void]
```

Find a function with an argument called ‘x’:

```groovy
gremlin> g.V().has('argument', 'name', 'x').out('function').valueMap('name')
==>[name:[increment]]
```

Et cetera, et cetera, et cetera…

## Some numbers

These are just some numbers mined from the `libLLVMCore.a`.

#### How many

| Number of functions | 71 019 |
|---|---|
| Number of basic blocks | 172 621 |
| Number of instructions | 1 212 322 |
| Number of types | 122 220 |

#### Top 10 instructions:

| call | 290 495 |
|---|---|
| load | 214 769 |
| store | 167 640 |
| alloca | 154 922 |
| br | 96 848 |
| getelementptr | 78 622 |
| ret | 67 729 |
| bitcast | 62 760 |
| icmp | 20 624 |
| phi | 9 716 |

#### Top 10 biggest functions:

| llvm::UpgradeIntrinsicCall(llvm::CallInst*, llvm::Function*) | 14033 |
|---|---|
| llvm::Intrinsic::getAttributes(llvm::LLVMContext&, unsigned int) | 8420 |
| ShouldUpgradeX86Intrinsic(llvm::Function*, llvm::StringRef) | 3635 |
| llvm::LLVMContextImpl::~LLVMContextImpl() | 2181 |
| UpgradeIntrinsicFunction1(llvm::Function*, llvm::Function*&) | 2006 |
| (anonymous namespace)::Verifier::visitIntrinsicCall(unsigned int, llvm::CallBase&) | 1887 |
| (anonymous namespace)::AssemblyWriter::printInstruction(llvm::Instruction const&) | 1869 |
| llvm::ConstantFoldBinaryInstruction(unsigned int, llvm::Constant*, llvm::Constant*) | 1244 |
| upgradeAVX512MaskToSelect(llvm::StringRef, llvm::IRBuilder&, llvm::CallInst&, llvm::Value*&) | 1073 |
| llvm::ConstantFoldGetElementPtr(llvm::Type*, llvm::Constant*, bool, llvm::Optional, llvm::ArrayRef) | 1055 |

## Resources

Here are some links if you want to learn more about Gremlin Queries and what’s possible:

- [Getting Started with TinkerPop](http://tinkerpop.apache.org/docs/3.4.6/tutorials/getting-started/)
- [Available Graph Traversals](http://tinkerpop.apache.org/docs/3.4.6/reference/#graph-traversal-steps)

## Next steps

Currently, the project is in its very early days, and many features are missing, to name a few: specific properties on instructions and values, def-use chains and other connections, complex constants (such as vectors of structs), and many more.

With that being said - [contributions are welcome](https://github.com/ShiftLeftSecurity/llvm2graphml)!
