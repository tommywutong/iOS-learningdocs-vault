---
title: Crash-free code with Fuzzer - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/crash-free-code-with-fuzzer/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a5d062308115a031'
translated: false
---

> 原文：[Crash-free code with Fuzzer - Low Level Bits 🇺🇦](https://lowlevelbits.org/crash-free-code-with-fuzzer/)　·　Low Level Bits (Alex Denisov)

# Crash-free code with Fuzzer

_Published on Mar 11, 2016_

We all know that the API has a specification. We all write tests to cover “happy paths” and to cover “unhappy paths” when work with the API.

It may seem that we’re pretty safe if we have tests and follow the specification. Well, actually no. Usually it works well in theory, but doesn’t really work in practice.

We can write as many tests as we need to cover all edge cases, but that is both time consuming and error prone. The best choice would be is to automate this process.

### Fuzzing

So we made a small library to make our life easier - [Fuzzer](https://github.com/AlexDenisov/Fuzzer).

The basic idea is to generate many many derivatives of original sample data and feed it to a consumer.

For instance, from this sample

```json
{
  "firstname" : "John",
  "lastname" : "Doe"
}
```

we could get two mutants by using `ReplaceNode` mutation, such as:

```json
{
  "firstname" : 42, // <- Mutation
  "lastname" : "Doe"
}
```

and

```json
{
  "firstname" : "John",
  "lastname" : 42 // <- Mutation
}
```

There are many decisions our serializer/mapper/whatnot can make when it gets such a result: return an error explaining why it cannot convert the dictionary into a model, or silently ignore “number” field, or any other action. In general this decision is up to you and your domain model. But I’m pretty sure there is no domain model that accepts exceptions like `-[__NSCFNumber length]: unrecognised selector sent to instance 0xDEADBEEF`.

### Usage

The use case may vary and depend on a workflow. The recommended way is to create another test target and put these verifications there.

Example:

```objectivec
- (void)test {
  NSDictionary *sample = @{
    @"name" : @"John Doe",
    @"age" : @42
  };

  UserDeserializer *deserializer = [UserDeserializer new];
  Mutator *mutator = [Mutator mutatorForSample:sample withMutationGenerator:[MutationGenerator builtinMutationGenerator]];
  Engine *engine = [Engine engineWithMutator:mutator];

  NSArray *reports = [engine runEngineOverMutants:^(NSDictionary *mutant) {
    User *user = [deserializer deserializeUser:mutant];
    user.name.length;
    user.age.integerValue;
  }];

  XCTAssertEqual(reports.count, 0);
}
```

It’s not very elegant, but it does the job very well. Lines like `user.name.length;` may look weird, but it’s the easiest way to validate that `name` is `NSString`.

_There might be a category `NSNull+length` or `NSNumber+length`, but AFAIK our team members doesn’t have such mutations._

Example looks pretty straightforward, but I’d like to highlight couple of things.

The block here does nothing but catching exceptions and recording them into internal storage within mutant that caused the exception:

```objectivec
NSArray *reports = [engine runEngineOverMutants:^(NSDictionary *mutant){ … }];
```

The engine records only failures, so it’s enough to assert count of returned reports. One can easily examine what caused failure by looking at report, e.g.:

```objectivec
for (Report *report in reports) {
  NSLog(@"Thrown '%@' on '%@'", report.exception, report.mutant);
}
```

### Builtins

The library provides just a couple of built-in mutations.

#### Delete Node Mutation

Returns sample without some node so that

```json
{
  "firstname" : "John",
  "lastname" : "Doe"
}
```

becomes either

```json
{
  "firstname" : "John"
}
```

or

```json
{
  "lastname" : "Doe"
}
```

#### Replace Node Mutation

This mutation replaces value of some node with another, ‘random’ value as shown in the very first example above.

‘Random’ quoted not because of nature of ‘randomness’ in general, but because the replacement can be provided using `NodeReplacement`, e.g.:

```objectivec
NodeReplacement *replacement = [NodeReplacement replacementWithValue:<#whatever may break your code#>];
id<Mutation> mutation = [ReplaceNodeMutation mutationWithReplacement:replacement];
```

That is, mutator will generate mutant with this replacement for each key/value.

### Extending Fuzzer

The library provides finite set of built-in mutations and replacements which is, probably, not enough for real life usage.

Fortunately, there is an easy way to extend it.

Previously we were changing only content of sample dictionary, now it’s time to go deeper (actually shallower).

Let’s create a mutation that will return random value (using `NodeReplacement`) instead of changing a sample.

Simplest interface ever:

```objectivec
#import <Fuzzer/Fuzzer.h>

@interface ReplaceSampleMutation : NSObject
  <Mutation>

+ (instancetype)mutationWithReplacement:(NodeReplacement *)replacement;

@end
```

Implementation is not sophisticated as well:

```objectivec
@interface ReplaceSampleMutation ()

@property NodeReplacement *replacement;

@end

@implementation ReplaceSampleMutation

///  Our constructor
+ (instancetype)mutationWithReplacement:(NodeReplacement *)replacement {
  ReplaceSampleMutation *mutation = [self new];

  mutation.replacement = replacement;

  return mutation;
}

/// ‘Mutation’ Protocol Requirement
- (NSDictionary *)mutateSample:(NSDictionary *)sample atNode:(NSString *)nodeName {
  return (NSDictionary *)self.replacement.value;
}

@end
```

The usage is trivial:

```objectivec
- (void)test {
  NSDictionary *sample = @{
    @"name" : @"John Doe",
    @"age" : @42
  };

  NSArray *replacements = [NodeReplacement builtinReplacements];

  NSMutableArray *mutations = [NSMutableArray arrayWithCapacity:replacements.count];
  for (NodeReplacement *replacement in replacements) {
        id<Mutation> mutation = [ReplaceSampleMutation mutationWithReplacement:replacement];
        [mutations addObject:mutation];
  }

  MutationGenerator *customGenerator = [MutationGenerator mutationGeneratorWithMutations:mutations];
  MutationGenerator *builtinGenerator = [MutationGenerator builtinMutationGenerator];

  MutationGenerator *mutationGenerator = [MutationGenerator combineMutationGenerators:@[ customGenerator, builtinGenerator ]];

  Mutator *mutator = [Mutator mutatorForSample:sample withMutationGenerator:mutationGenerator];
  Engine *engine = [Engine engineWithMutator:mutator];

  UserDeserializer *deserializer = [UserDeserializer new];
  NSArray *reports = [engine runEngineOverMutants:^(NSDictionary *mutant) {
    User *user = [deserializer deserializeUser:mutant];
    user.name.length;
    user.age.integerValue;
  }];

  XCTAssertEqual(reports.count, 0);
}
```

### That’s pretty much it

Please, don’t crash when your server lies!

P.S. I do consider to include `ReplaceSampleMutation` into the set of built-in mutations. I will be more than happy to review the [Pull Request](https://github.com/AlexDenisov/Fuzzer).
