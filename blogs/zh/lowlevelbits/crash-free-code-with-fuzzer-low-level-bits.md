---
title: 使用 Fuzzer 编写无崩溃代码 - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/crash-free-code-with-fuzzer/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a5d062308115a031'
translated: true
---

> 原文：[Crash-free code with Fuzzer - Low Level Bits 🇺🇦](https://lowlevelbits.org/crash-free-code-with-fuzzer/)　·　Low Level Bits (Alex Denisov)

# 使用 Fuzzer 编写无崩溃代码（Crash-free code with Fuzzer）

_发布于 2016 年 3 月 11 日_

我们都知道 API 是有规范的。我们也都编写测试来覆盖“愉快路径（happy paths）”和与 API 交互时的“不愉快路径（unhappy paths）”。

如果有测试并且遵循规范，我们可能觉得自己相当安全了。嗯，实际上并非如此。通常这在理论上会工作良好，但在实践中却不尽如人意。

我们可以编写尽可能多的测试来覆盖所有边界情况，但这既耗时又容易出错。最好的选择是让这个过程自动化。

### 模糊测试（Fuzzing）

所以我们做了一个小库来让生活更轻松——[Fuzzer](https://github.com/AlexDenisov/Fuzzer)。

基本思路是生成原始样本数据的许多许多变体，并将其输入给消费者（consumer）。

例如，从这个样本

```json
{
  "firstname" : "John",
  "lastname" : "Doe"
}
```

我们可以通过使用 `ReplaceNode` 变异（mutation）得到两个突变体（mutant），例如：

```json
{
  "firstname" : 42, // <- Mutation
  "lastname" : "Doe"
}
```

和

```json
{
  "firstname" : "John",
  "lastname" : 42 // <- Mutation
}
```

我们的序列化器/映射器/其他组件在得到这样的结果时，可能会做出许多决定：返回一个错误说明为何无法将字典转换为模型，或静默忽略“number”字段，或执行其他任何操作。通常，这个决定取决于你和你的领域模型。但我相当肯定，没有任何领域模型能接受像 `-[__NSCFNumber length]: unrecognised selector sent to instance 0xDEADBEEF` 这样的异常。

### 用法

用例可能会因工作流程而异。推荐的方式是创建另一个测试 target，然后将这些验证放在那里。

示例：

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

这并不十分优雅，但它很好地完成了任务。像 `user.name.length;` 这样的代码行可能看起来很奇怪，但这是验证 `name` 是 `NSString` 的最简单方法。

_可能会有 `NSNull+length` 或 `NSNumber+length` 这样的分类（category），但据我所知，我们的团队成员并没有这样的变异。_

这个示例看起来相当直接，但我想要强调几点。

这里的 `block` 除了捕获异常并将其记录到导致该异常的突变体内部的存储中外，不做其他任何事情：

```objectivec
NSArray *reports = [engine runEngineOverMutants:^(NSDictionary *mutant){ … }];
```

引擎只记录失败情况，因此只需断言返回报告的计数就足够了。我们可以通过查看报告来轻松检查失败的原因，例如：

```objectivec
for (Report *report in reports) {
  NSLog(@"Thrown '%@' on '%@'", report.exception, report.mutant);
}
```

### 内置变异（Builtins）

该库仅提供少量内置变异。

#### 删除节点变异（Delete Node Mutation）

返回不带某个节点的样本，以便

```json
{
  "firstname" : "John",
  "lastname" : "Doe"
}
```

变成

```json
{
  "firstname" : "John"
}
```

或

```json
{
  "lastname" : "Doe"
}
```

#### 替换节点变异（Replace Node Mutation）

该变异将某个节点的值替换为另一个“随机”值，如上文第一个示例所示。

这里的“随机”加引号，并非因为“随机性”本身的性质，而是因为替换可以通过 `NodeReplacement` 提供，例如：

```objectivec
NodeReplacement *replacement = [NodeReplacement replacementWithValue:<#whatever may break your code#>];
id<Mutation> mutation = [ReplaceNodeMutation mutationWithReplacement:replacement];
```

也就是说，变异器（mutator）将为每个键/值生成带有此替换的突变体。

### 扩展 Fuzzer

该库提供了一组有限的内置变异和替换，这对于实际使用可能不够。

幸运的是，扩展它很容易。

之前我们只改变样本 dictionary 的内容，现在是时候深入（实际上是浅出）了。

让我们创建一个变异（使用 `NodeReplacement`）来返回随机值，而不是更改样本。

最简单的接口：

```objectivec
#import <Fuzzer/Fuzzer.h>

@interface ReplaceSampleMutation : NSObject
  <Mutation>

+ (instancetype)mutationWithReplacement:(NodeReplacement *)replacement;

@end
```

实现也同样不复杂：

```objectivec
@interface ReplaceSampleMutation ()

@property NodeReplacement *replacement;

@end

@implementation ReplaceSampleMutation

///  我们的构造函数
+ (instancetype)mutationWithReplacement:(NodeReplacement *)replacement {
  ReplaceSampleMutation *mutation = [self new];

  mutation.replacement = replacement;

  return mutation;
}

/// ‘Mutation’ 协议要求
- (NSDictionary *)mutateSample:(NSDictionary *)sample atNode:(NSString *)nodeName {
  return (NSDictionary *)self.replacement.value;
}

@end
```

使用起来很简单：

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

### 基本就是这样

当你的服务器撒谎时，请不要崩溃！

附注：我正在考虑将 `ReplaceSampleMutation` 纳入内置变异集。我将非常乐意审查[拉取请求（Pull Request）](https://github.com/AlexDenisov/Fuzzer)。
