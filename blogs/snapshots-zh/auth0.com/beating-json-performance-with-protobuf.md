---
title: 使用 Protobuf 超越 JSON 性能
source_url: 'https://auth0.com/blog/beating-json-performance-with-protobuf/'
source_domain: auth0.com
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:f803eb4130eacfca'
plan_ref: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天） / Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09）
plan_week: 第八阶段：持久化、序列化、源码、架构与网络串联（建议 10 天）
plan_day: Day 3｜序列化先比较需求，再看二进制细节（对应 W5-09）
container: //article
container_source: guess
---

> 原文：[Beating JSON performance with Protobuf](https://auth0.com/blog/beating-json-performance-with-protobuf/)

**TL;DR**

Protocol buffers（协议缓冲区，简称 Protobuf）是一种由 Google 创建的二进制格式，用于在不同的服务之间对数据进行序列化。Google 将此协议开源，目前它已原生支持最常见的语言，如 JavaScript、Java、C#、Ruby 等。在我们的测试中，该协议的性能比 JSON 快**最多 6 倍**。

> “Protobuf 的性能比 JSON 快最多 6 倍。”
>
> [Tweet This](https://twitter.com/intent/tweet?text="Protobuf%20performs%20up%20to%206%20times%20faster%20than%20JSON." via @auth0 https://auth0.com/blog/beating-json-performance-with-protobuf)

## 什么是 Protobuf

[Protocol buffers](https://developers.google.com/protocol-buffers/docs/overview)，通常称为 Protobuf，是由 Google 开发的一种协议，用于结构化数据的序列化和反序列化。Google 开发它的目标是提供一种比 XML 更好的方式，使系统能够通信。因此，他们专注于使其比 XML 更简单、更小、更快且更易于维护。但是，正如你将在这篇文章中看到的，该协议甚至超越了 JSON，具有更好的性能、更好的可维护性和更小的体积。

### 它与 JSON 有何不同？

需要注意的是，虽然 [JSON](http://www.json.org/) 和 [Protobuf](https://developers.google.com/protocol-buffers/docs/overview) 消息可以互换使用，但这些技术的设计目标不同。JSON（JavaScript Object Notation）只是一种从 JavaScript 编程语言子集衍生而来的消息格式。JSON 消息以文本格式交换，如今它已完全独立，并且几乎所有编程语言都支持它。

另一方面，Protobuf 不仅仅是一种消息格式，它还是一套用于定义和交换这些消息的规则和工具。该协议的创建者 Google 已将其开源，并提供了为目前最常用的编程语言生成代码的工具，例如 [JavaScript](https://developers.google.com/protocol-buffers/docs/reference/javascript-generated)、[Java](https://developers.google.com/protocol-buffers/docs/javatutorial)、[PHP](https://developers.google.com/protocol-buffers/docs/reference/php-generated)、[C#](https://developers.google.com/protocol-buffers/docs/csharptutorial)、[Ruby](https://developers.google.com/protocol-buffers/docs/reference/ruby-generated)、[Objective C](https://developers.google.com/protocol-buffers/docs/reference/objective-c-generated)、[Python](https://developers.google.com/protocol-buffers/docs/pythontutorial)、[C++](https://developers.google.com/protocol-buffers/docs/cpptutorial) 和 [Go](https://developers.google.com/protocol-buffers/docs/gotutorial)。除此之外，Protobuf 拥有比 JSON 更多的数据类型，例如枚举和方法，并且还广泛用于 [RPC（远程过程调用）](https://github.com/grpc)。

## Protobuf 真的比 JSON 快吗？

网上有一些资源表明 Protobuf 的性能优于 JSON、XML 等——例如[这个](https://github.com/eishay/jvm-serializers/wiki)和[这个](https://maxondev.com/serialization-performance-comparison-c-net-formats-frameworks-xmldatacontractserializer-xmlserializer-binaryformatter-json-newtonsoft-servicestack-text/)——但检查一下是否适合自己的需求和用例总是很重要的。在 [Auth0](https://auth0.com/)，我开发了一个简单的 [Spring Boot 应用程序](https://github.com/brunokrebs/auth0-speed-test)来测试几个场景，并衡量 JSON 和 Protobuf 的性能。我主要测试了两种协议的序列化，以便让两个 Java 应用程序通信，以及让一个 JavaScript Web 应用程序与这个后端通信。

> 创建这两个场景（Java 到 Java 和 JavaScript 到 Java）的主要原因是为了衡量该协议在 Java 这样的企业环境中，以及在 JSON 是原生消息格式的环境中的表现。也就是说，我在这里展示的数据来自两种环境：一种是 JSON 内建且应该运行极快的环境（JavaScript 引擎），另一种是 JSON 并非一等公民的环境。

对这个问题的简短回答是：是的，Protobuf 比 JSON 快。但是，如果没有我的实验收集的数据，这个答案既没有用也不有趣。现在让我们来看看细节。

### 测试样本

为了支持测量，我创建了三个 Protobuf 消息：`Address`，仅包含街道和门牌号；`Person`，包含姓名、地址集合、手机号码集合和电子邮件地址集合；`People`，包含 `Person` 消息的集合。这些消息被组装在一个具有四个 RESTful 端点（endpoint）的应用程序中：

1. 一个接受 `GET` 请求并以 Protobuf 格式返回 5 万人的列表。
2. 另一个接受 `GET` 请求并以 JSON 格式返回相同的 5 万人列表。
3. 第三个接受 `POST` 请求，包含任意数量的 Protobuf 格式的人。
4. 第四个接受 `POST` 请求，包含任意数量的 JSON 格式的人。

### JavaScript 到 Java 的通信

由于有许多 JavaScript 引擎可用，了解最流行的引擎如何处理这组数据是很有价值的。因此，我决定使用以下浏览器：[Chrome](https://www.google.com/chrome)，因为它是最流行的浏览器，其 JavaScript 引擎也被 [Node.js](https://nodejs.org) 使用；[Firefox](https://www.mozilla.org/en-US/firefox/new/)，作为另一个非常流行的浏览器；以及 [Safari](https://www.apple.com/safari/)，作为 MacBook 和 iPhone 上的默认浏览器。

以下图表展示了这些浏览器在向两个端点（Protobuf 和 JSON）发出 50 次连续的 `GET` 请求时的平均性能。每个端点的这 50 次请求执行了两次：第一次在 Spring Boot 应用程序启用压缩的情况下运行，第二次在关闭压缩的情况下运行。所以，最终每个浏览器请求了 200 次这 5 万人的数据。

![压缩 GET 请求下 Protobuf/JSON 性能对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/e25156d80ff22816eb57.png)

![压缩 GET 请求下 Protobuf/JSON 负载大小对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/ac97d1edaeeda91a670a.png)

正如你在上面的图表中看到的，在**压缩环境下**，Protobuf 和 JSON 的结果非常相似。Protobuf 消息比 JSON 消息**小了 9%**，并且它们传递到 JavaScript 代码所用的时间**仅少 4%**。这听起来可能不算什么，但考虑到 Protobuf 必须从二进制转换为 JSON（JavaScript 代码使用 JSON 作为其对象字面量格式），Protobuf 能够比它的对手更快已经非常了不起了。

现在，当我们处理**非压缩消息**时，结果发生了相当大的变化。让我们分析下面的图表：

![非压缩 GET 请求下 Protobuf/JSON 性能对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/fd69fb93c6ae638317fb.png)

![非压缩 GET 请求下 Protobuf/JSON 负载大小对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/85b31b39a49dde26274c.png)

在这些情况下，与 JSON 相比，Protobuf 的表现甚至更好。这种格式的消息**小了 34%**，并且它们传递到 JavaScript 代码所用的时间**少了 21%**。

当发出 `POST` 请求时，差异几乎变得难以察觉，因为这种类型的请求通常不处理重量级消息。通常，这些请求只处理表单中几个字段的更新或类似操作。因此，为了使测试可信，我发出了 50 个请求，每个请求只包含一个 `Person` 消息和一些属性，例如电子邮件地址和手机号。结果如下：

![POST 请求下 Protobuf/JSON 性能对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/a2f8610a21e787e528e8.png)

![POST 请求下 Protobuf/JSON 负载大小对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/8d4ec3df516cdab2b977.png)

在这种情况下，消息大小甚至没有差异，主要是因为它们太小，以至于关于它们的元数据比数据本身更重。发出请求并得到响应的时间也几乎相等，Protobuf 请求与 JSON 请求相比，性能**仅好 4%**。

### Java 到 Java 的通信

如果我们只使用 JavaScript 环境（如 Node.js 应用程序和 Web 浏览器作为接口），我会在投入时间学习和将端点迁移到 Protobuf 之前三思。但是，当我们开始添加其他平台，如 Java、Android、Python 等时，我们才开始看到使用 Protobuf 的真正收益。

下面的图表是由一个 Spring Boot 应用程序向另一个 Spring Boot 应用程序发出的 500 个 `GET` 请求的平均性能生成的。两个应用程序部署在 [Digital Ocean](https://www.digitalocean.com/) 托管的不同虚拟机上。我选择这种策略是为了模拟两个微服务通过网络通信的常见场景。让我们看看这个模拟的运行情况：

![由一个 Java 应用程序向另一个 Java 应用程序发出的 GET 请求下 Protobuf/JSON 性能对比](../../../attachments/snapshots/auth0.com/99d33eb90cba/150367ae446ceb9b4d61.png)

这是一个巨大的性能提升。在**非压缩**环境中使用 Protobuf 时，请求所用的时间比 JSON 请求**少了 78%**。这表明二进制格式的性能比文本格式快了**近 5 倍**。而且，在**压缩**环境中发出这些请求时，差异甚至更大。Protobuf 的性能**快 6 倍**，处理 JSON 格式需要 150ms 的请求，它只需要 25ms。

如你所见，当我们所处环境不是 JSON 的原生环境时，性能提升是巨大的。因此，每当你遇到 JSON 的延迟问题时，考虑迁移到 Protobuf。

## 还有其他优点和缺点吗？

正如你所做的每一个决定，都会有优点和缺点。而在选择一种消息格式或协议而不是另一种时，也不例外。Protobuf 存在一些问题，我列举如下：

- **资源匮乏**。你不会找到太多关于使用和开发 Protobuf 的资源（不要期望有非常详细的文档或太多的博文）。
- **社区较小**。这可能是第一个缺点的根本原因。例如，在 Stack Overflow 上，你会发现大约有 1500 个标记为 Protobuf 的问题。而在同一平台上，JSON 的问题超过 18 万个。
- **支持有限**。Google 不支持其他编程语言，如 Swift、R、Scala 等。但是，有时你可以通过第三方库来克服这个问题，例如 [Apple 提供的 Swift Protobuf](https://github.com/apple/swift-protobuf)。
- **人类不可读**。JSON 以文本格式交换且结构简单，易于人类阅读和分析。二进制格式则不然。

虽然选择 Protobuf 会带来这些缺点，但正如我上面演示的，该协议在某些情况下要快得多。除此之外，还有其他一些优点：

- **正式格式**。格式是自描述的。
- **RPC 支持**。服务器 RPC 接口可以作为协议文件的一部分进行声明。
- **结构验证**。拥有预定义的且比 JSON 更大的数据集类型，通过 Protobuf 序列化的消息可以由负责交换它们的代码自动验证。

## 如何使用 Protobuf？

既然你已经知道 Protobuf 比 JSON 快，并且也了解了它的优点和缺点，让我们来看看如何使用这项技术。Protobuf 有三个主要组成部分需要我们处理：

1. **消息描述符**。使用 Protobuf 时，我们必须在 `.proto` 文件中定义我们的消息结构。
2. **消息实现**。仅仅有消息定义不足以在任何编程语言中表示和交换数据。我们必须生成类/对象来处理所选编程语言中的数据。幸运的是，Google 为最常见的编程语言提供了代码生成器。
3. **解析与序列化**。定义和创建 Protobuf 消息后，我们需要能够交换这些消息。只要我们使用一种受支持的编程语言，Google 会再次帮助我们。

让我们简要了解每个组成部分。

### Protobuf 消息定义

如前所述，Protobuf 中的消息在 `.proto` 文件中描述。下面你可以找到我在性能测试中使用的三个消息描述符的示例。我将它们全部定义在同一个文件中，我将其命名为 `people.proto`。

```
syntax = "proto3";

package demo;

option java_package = "com.auth0.protobuf";

message People {
    repeated Person person = 1;
}

message Person {
    string name = 1;
    repeated Address address = 2;
    repeated string mobile = 3;
    repeated string email = 4;
}

message Address {
    string street = 1;
    int32 number = 2;
}
```

上面的三个消息非常简单易懂。第一个消息 `People` 只包含一个 `Person` 消息的集合。第二个消息 `Person` 包含一个 `string` 类型的 `name`，一个 `Address` 消息的集合，一个以 `string` 形式保存的 `mobile` 号码集合，以及一个同样以 `string` 形式保存的 `email` 地址集合。第三个消息 `Address` 包含两个属性：第一个是 `string` 类型的 `street`；第二个是 `int32` 类型的 `number`。

除了这些定义之外，文件顶部还有三行有助于代码生成器的内容：

1. 首先是一个值为 `proto3` 的 `syntax` 定义。这是我使用的 Protobuf 版本，在撰写本文时，它是最新版本。需要注意的是，早期版本的 Protobuf 曾经允许开发者通过使用 `required` 关键字对他们交换的消息进行更严格的限制。这现在已被废弃，不再可用。
2. 其次是 `package demo;` 定义。此配置用于嵌套创建的生成类/对象。
3. 第三，有一个 `option java_package` 定义。生成器也使用此配置来嵌套生成的源代码。这里的区别是，这仅适用于 Java。我同时使用了这两个配置，以使生成器在为 Java 创建代码和为 JavaScript 创建代码时表现不同。也就是说，Java 类创建在 `com.auth0.protobuf` 包中，而 JavaScript 对象创建在 `demo` 之下。

Protobuf 还有更多可用的选项和数据类型。Google 在[此处](https://developers.google.com/protocol-buffers/docs/proto3)有关于这方面的非常好的文档。

### 消息实现

为了生成 `proto` 消息的源代码，我使用了两个库：

1. 对于 Java，我使用了 Google 提供的 `Protocol Compiler`。[Protocol Buffers 文档中的此页面](https://developers.google.com/protocol-buffers/docs/downloads)说明了如何安装它。因为我在 MacBook 上使用 [Brew](http://brew.sh/)，所以只需执行 `brew install protobuf` 即可。
2. 对于 JavaScript，我使用了 `protobuf.js`。你可以[在此处](https://github.com/dcodeIO/protobuf.js)找到其源代码和说明。

对于大多数受支持的编程语言，如 Python、C# 等，Google 的 `Protocol Compiler` 已经足够。但对于 JavaScript，`protobuf.js` 更好，因为它有更好的文档、[更好的支持](https://github.com/dcodeIO/protobuf.js/blob/2db4305ca67d003d57aa14eb23f25eb6c3672034/README.md#compatibility)和更好的性能——我也使用 Google 提供的默认库运行了性能测试，但结果比使用 JSON 更差。

### 使用 Java 进行解析与序列化

安装 `Protocol Compiler` 后，我使用以下命令生成了 Java 源代码：

```bash
protoc --java_out=./src/main/java/ ./src/main/resources/people.proto
```

我从项目的根路径发出此命令，并添加了两个参数：`java_out`，将 `./src/main/java/` 定义为 Java 代码的输出目录；以及 `./src/main/resources/people.proto`，这是 `.proto` 文件的路径。

生成的代码相当复杂，但幸运的是，它的使用并不复杂。对于每个编译的消息，都会生成一个构建器（builder）。看看这有多简单：

```java
final Address address1 = Address.newBuilder()
        .setStreet("Street Number " + i)
        .setNumber(i)
        .build();

final Address address2 = Address.newBuilder()
        .setStreet("Street Number " + i)
        .setNumber(i)
        .build();

final Person person = Person.newBuilder()
        .setName("Person Number " + i)
        .addMobile("111111" + i)
        .addMobile("222222" + i)
        .addEmail("emailperson" + i + "@somewhere.com")
        .addEmail("otheremailperson" + i + "@somewhere.com")
        .addAddress(address1)
        .addAddress(address2)
        .build();
```

这些实例本身只代表消息，所以我还需要一种方法来交换它们。Spring 提供了对 Protobuf 的支持，并且网络上有一些资源——例如 [Spring 博客上的这篇](https://spring.io/blog/2015/03/22/using-google-protocol-buffers-with-spring-mvc-based-rest-services)和 [Baeldung 上的这篇](http://www.baeldung.com/spring-rest-api-with-protocol-buffers)——在这方面帮助了我。请注意，与任何 Java 项目一样，需要一些依赖项。以下是我必须添加到 Maven 项目中的依赖项：

```text
<dependencies>
    <!-- Spring Boot deps and etc above.. -->
    <dependency>
        <groupId>com.google.protobuf</groupId>
        <artifactId>protobuf-java</artifactId>
        <version>3.1.0</version>
    </dependency>

    <dependency>
        <groupId>com.google.protobuf</groupId>
        <artifactId>protobuf-java-util</artifactId>
        <version>3.1.0</version>
    </dependency>

    <dependency>
        <groupId>com.googlecode.protobuf-java-format</groupId>
        <artifactId>protobuf-java-format</artifactId>
        <version>1.4</version>
    </dependency>
</dependencies>
```

### 使用 JavaScript 进行解析与序列化

使用的库 `protobuf.js` 帮助我将 `.proto` 消息编译成 JavaScript，并帮助我交换这些消息。我需要做的第一件事是将其安装为依赖项。为此，我使用了 [Node.js](https://nodejs.org) 和 [NPM](https://www.npmjs.com)：

```bash
npm install -g protobufjs
```

上面的命令使我能够使用 `pbjs` 命令行工具（CLI）来生成代码。以下是我使用此 CLI 的方式：

```bash
pbjs -t static-module -w commonjs -o \
    ./src/main/resources/static/people.js \
    ./src/main/resources/people.proto
```

生成 JavaScript 代码后，我使用另一个工具 [`browserify`](http://browserify.org/) 将生成的代码与 `protobuf.js` 打包到单个文件中：

```bash
# Installing browserify globally to use wherever I want.
npm install -g browserify
# Running browserify to bundle protobuf.js and message objects together.
browserify ./src/main/resources/static/people.js -o ./src/main/resources/static/bundle.js
```

通过这样做，我能够向我的 `index.html` 文件添加单个依赖项：

```text
<html>
<body>
  <!-- This has all my protobuf dependecies: three messages and protobuf.js code. -->
  <script src="bundle.js"></script>
</body>
</html>
```

最后，在引用该包之后，我就可以向我的 Protobuf 端点发出 `GET` 和 `POST` 请求了。以下代码是一个 AngularJS HTTP `GET` 请求，因此应该非常容易理解：

```text
// Just a shortcut.
const People = protobuf.roots.default.demo.People;

let req = {
  method: 'GET',
  responseType: 'arraybuffer', // make it clear that it can handle binary
  url: '/some-protobuf-get-endpoint'
};
return $http(req).then(function(response) {
  // We need to encapsulate the response on Uint8Array to avoid
  // getting it converted to string.
  ctrl.people = People.decode(new Uint8Array(response.data)).person;
});
```

`POST` 请求也同样简单：

```text
// Just populating some usual object literals.
let address = new Address({
  street: 'Street',
  number: 100
});

let person = {
  name: 'Some person',
  address: [],
  mobile: [],
  email: []
};

person.address.push(address);
person.mobile.push('(1) 732-757-2923');
person.email.push('someone@somewhere.com');

// Encapsulating the object literal inside the protobuf object.
let people = new People({
  person: [new Person(person)]
});

// Building the POST request.
let post = {
  method: 'POST',
  url: '/some-protobuf-post-endpoint',
  // Transforming to binary.
  data: People.encode(people).finish(),
  // Avoiding AngularJS to parse the data to JSON.
  transformRequest: [],
  headers: {
    // Tells the server that a protobuf message is being transmitted.
    'Content-Type': 'application/x-protobuf'
  }
};

// Issuing the POST request built above.
return $http(post).then(function() {
  console.log('Everything went just fine');
});
```

使用 `protobuf.js` 库来交换二进制数据并不难，对吧？如果你想，你也可以直接在我的 [GitHub 仓库](https://github.com/brunokrebs/auth0-speed-test/blob/master/src/main/resources/static/index.html#L46)中查看我用来比较 Protobuf 和 JSON 性能的 JavaScript 代码。

## 附：使用 Auth0 保护 Node.js 应用程序

使用 Auth0 保护 Node.js 应用程序很容易，并且带来了许多很棒的特性。使用 [Auth0](https://auth0.com/)，我们只需编写几行代码，就能获得可靠的[身份管理解决方案](https://auth0.com/user-management)、[单点登录](https://auth0.com/docs/sso/single-sign-on)、对[社交身份提供商（如 Facebook、GitHub、Twitter 等）](https://auth0.com/docs/identityproviders)的支持，以及对[企业身份提供商（如 Active Directory、LDAP、SAML、自定义等）](https://auth0.com/enterprise)的支持。

在接下来的部分中，我们将学习如何使用 Auth0 保护用 [Express](https://expressjs.com/) 编写的 Node.js API。

### 创建 Express API

让我们从定义我们的 Node.js API 开始。使用 Express 和 Node.js，我们可以通过两个简单的步骤来完成。第一步是使用 [NPM](https://www.npmjs.com/) 安装三个依赖项：`npm i express body-parser cors`。

> **注意：** 如果是从头开始，我们必须首先初始化一个 NPM 项目：`npm init -y`。这将使 NPM 在当前目录中创建一个新项目。因此，在运行此命令之前，我们必须为我们的新项目创建一个新目录并进入它。

第二步是使用以下代码创建一个 Node.js 脚本（我们可以称之为 `index.js`）：

```text
// importing dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

// configuring Express
const app = express();
app.use(bodyParser.json());
app.use(cors());

// defining contacts array
const contacts = [
  { name: 'Bruno Krebs', phone: '+555133334444' },
  { name: 'John Doe', phone: '+191843243223' },
];

// defining endpoints to manipulate the array of contacts
app.get('/contacts', (req, res) => res.send(contacts));
app.post('/contacts', (req, res) => {
  contacts.push(req.body);
  res.send();
});

// starting Express
app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

上面的代码创建了 Express 应用程序，并向其添加了两个中间件：`body-parser` 用于解析 JSON 请求，以及 `cors` 用于表示应用程序接受来自任何来源的请求。该应用程序还在 Express 上注册了两个端点来处理 POST 和 GET 请求。两个端点都使用 `contacts` 数组作为某种内存数据库。

现在，我们可以通过在项目根目录下执行 `node index` 并向其提交请求来运行和测试我们的应用程序。例如，使用 [cURL](https://curl.haxx.se/)，我们可以通过执行 `curl localhost:3000/contacts` 发送 GET 请求。此命令将输出 `contacts` 数组中的项目。

### 在 Auth0 注册 API

创建我们的应用程序后，我们可以专注于保护它。让我们首先在 Auth0 上注册一个 API 来表示我们的应用程序。为此，让我们前往[管理仪表板的 API 部分](https://manage.auth0.com/#/apis)（如果需要，我们可以创建一个[免费账户](https://auth0.com/signup)），然后点击“Create API”。在出现的对话框中，我们可以将我们的 API 命名为“Contacts API”（名称并不重要），并将其标识为 `https://contacts.blog-samples.com/`（我们稍后将使用此值）。

### 使用 Auth0 保护 Express

现在我们已经在我们 Auth0 账户中注册了 API，让我们使用 Auth0 保护 Express API。让我们首先使用 NPM 安装三个依赖项：`npm i express-jwt jwks-rsa`。然后，让我们创建一个名为 `auth0.js` 的文件并使用这些依赖项：

```text
const jwt = require('express-jwt');
const jwksRsa = require('jwks-rsa');

module.exports = jwt({
  // Fetch the signing key based on the KID in the header and
  // the singing keys provided by the JWKS endpoint.
  secret: jwksRsa.expressJwtSecret({
    cache: true,
    rateLimit: true,
    jwksUri: `https://${process.env.AUTH0_DOMAIN}/.well-known/jwks.json`,
  }),

  // Validate the audience and the issuer.
  audience: process.env.AUTH0_AUDIENCE,
  issuer: `https://${process.env.AUTH0_DOMAIN}/`,
  algorithms: ['RS256'],
});
```

此脚本的目标是导出一个 [Express 中间件](http://expressjs.com/en/guide/using-middleware.html)，该中间件保证请求具有由可信方（在本例中为 Auth0）颁发的 `access_token`。请注意，此脚本期望找到两个环境变量：

- `AUTH0_AUDIENCE`：我们 API 的标识符（`https://contacts.mycompany.com/`）
- `AUTH0_DOMAIN`：我们在 Auth0 的域名（在我的例子中是 `bk-samples.auth0.com`）

我们很快会设置这些变量，但重要的是要理解域名变量定义了中间件如何查找签名密钥。

创建此中间件后，我们可以更新 `index.js` 文件以导入并使用它：

```text
// ... other require statements ...
const auth0 = require('./auth0');

// ... app definition and contacts array ...

// redefining both endpoints
app.get('/contacts', auth0(), (req, res) => res.send(contacts));
app.post('/contacts', auth0(), (req, res) => {
  contacts.push(req.body);
  res.send();
});

// ... app.listen ...
```

在这种情况下，我们替换了之前定义的端点，以使用新的中间件，该中间件强制要求请求必须带有有效的访问令牌（access token）发送。

现在运行应用程序略有不同，因为我们需要设置环境变量：

```bash
export AUTH0_DOMAIN=blog-samples.auth0.com
export AUTH0_AUDIENCE="https://contacts.blog-samples.com/"
node index
```

运行 API 后，我们可以测试它是否被正确保护。所以，让我们打开一个终端并执行以下命令：

```bash
curl localhost:3000/contacts
```

如果我们正确设置了所有内容，我们将收到来自服务器的响应，提示“no authorization token was found”。

现在，为了能够再次与我们的端点交互，我们必须从 Auth0 获取一个访问令牌。有多种方法可以做到这一点，[我们使用的策略将取决于我们正在开发的客户端应用程序的类型](https://auth0.com/docs/api-auth/which-oauth-flow-to-use)。例如，如果我们正在开发一个单页应用程序（SPA），我们将使用所谓的 [_Implicit Grant_](https://auth0.com/docs/api-auth/tutorials/implicit-grant)。如果我们正在开发一个移动应用程序，我们将使用 [_Authorization Code Grant Flow with PKCE_](https://auth0.com/docs/api-auth/tutorials/authorization-code-grant-pkce)。Auth0 还有其他可用的流程。然而，对于像这样的简单测试，我们可以使用我们的 Auth0 仪表板来获取一个。

因此，我们可以回到 [Auth0 仪表板的 _APIs_ 部分](https://manage.auth0.com/#/apis)，点击我们之前创建的 API，然后点击该 API 的 _Test_ 部分。在那里，我们会找到一个名为 _Copy Token_ 的按钮。让我们点击这个按钮，将访问令牌复制到剪贴板。

![从 Auth0 仪表板复制测试令牌。](../../../attachments/snapshots/auth0.com/99d33eb90cba/7d3a658a76c626e01c26.png)

复制此令牌后，我们可以打开一个终端并执行以下命令：

```bash
# create a variable with our token
ACCESS_TOKEN=<OUR_ACCESS_TOKEN>

# use this variable to fetch contacts
curl -H 'Authorization: Bearer '$ACCESS_TOKEN http://localhost:3000/contacts/
```

> **注意：** 我们需要将 `<OUR_ACCESS_TOKEN>` 替换为我们从仪表板复制的令牌。

由于我们现在在发送给 API 的请求中使用了我们的访问令牌，我们将能够再次获取联系人列表。

这就是我们保护 Node.js 后端 API 的方法。很简单，对吧？

## 结论

老实说，我原本希望 Protobuf 有更有利的表现。当然，在 Java 到 Java 的通信中，使用 Protobuf 能够在 25ms 内处理 5 万个 `Person` 对象实例，而 JSON 需要 150ms，这非常了不起。但在 JavaScript 环境中，这些收益要低得多。

> “Protobuf 协议在服务间交换数据可以带来巨大的性能提升。”
>
> [Tweet This](https://twitter.com/intent/tweet?text="Protobuf%20protocol%20to%20exchange%20data%20between%20services%20can%20bring%20great%20performance." via @auth0 https://auth0.com/blog/beating-json-performance-with-protobuf)

尽管如此，考虑到 JSON 是 JavaScript 引擎的原生格式，Protobuf 仍然设法做到了更快。

另外，我注意到的一件重要事情是，尽管关于 Protobuf 的资源不多，我仍然能够毫无困难地在不同环境中使用它。所以我想从现在开始我会更频繁地使用这项技术。

你呢？你对 Protobuf 的速度有什么看法？你正在考虑在你的项目中使用它吗？留下评论！

> 你正在使用 XXX 构建产品吗？我们在 Auth0 可以帮助你专注于对你来说最重要的事情，即你产品的特殊功能。[Auth0](https://auth0.com/) 可以帮助你通过最先进的功能（如[无密码](https://auth0.com/passwordless)、[泄露密码监控](https://auth0.com/breached-passwords)和[多因素认证](https://auth0.com/multifactor-authentication)）来保护你的产品安全。[我们提供慷慨的**免费层级**](https://auth0.com/pricing)来开始使用现代认证。

关于作者

![Bruno Krebs](../../../attachments/snapshots/auth0.com/99d33eb90cba/005b400c7301046c537d.jpg)

#### Bruno Krebs

研发内容架构师 (Auth0 Alumni)

我热衷于开发高度可扩展、有弹性的应用程序。我喜欢从数据库到微服务 (Kubernetes, Docker 等) 再到前端的方方面面。我觉得思考所有部分如何协同工作以为最终用户提供快速愉悦的体验是非常神奇的，主要是因为他们完全不知道那个“简单”的 app 有多复杂。[查看个人资料](https://auth0.com/blog/authors/bruno-krebs/)
