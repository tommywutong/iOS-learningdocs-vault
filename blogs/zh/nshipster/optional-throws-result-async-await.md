---
title: Optional、throws、Result 与 async/await
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/optional-throws-result-async-await/'
original_language: en
published: 2019-04-29
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:9a00a969ca8960f5'
translated: true
---

> 原文：[Optional、throws、Result 与 async/await](https://nshipster.com/optional-throws-result-async-await/)　·　NSHipster (Mattt)

# [Optional、throws、Result 与 async/await](https://nshipster.com/optional-throws-result-async-await/)

作者：[jemmons](https://nshipster.com/authors/jemmons/)　2019 年 4 月 29 日

在 Swift 1 的早期，我们并没有多少错误处理手段。不过我们有 `Optional`，而且感觉很棒！将 null 检查显式化并强制执行后，通过返回 `nil` 直接退出函数不再像代码异味，而更像一种语言特性。

下面是一个小型实用函数：它获取 Keychain 数据，任何错误都返回 `nil`：

```
func keychainData(service: String) -> Data? {
  let query: NSDictionary = [
    kSecClass: kSecClassGenericPassword,
    kSecAttrService: service,
    kSecReturnData: true
  ]
  var ref: CFTypeRef? = nil

  switch SecItemCopyMatching(query, &ref) {
  case errSecSuccess:
    return ref as? Data
  default:
    return nil
  }
}
```

我们设置查询，将一个空的 `inout` 引用传给 `SecItemCopyMatching`，然后根据返回的状态码，要么将该引用作为数据返回，要么在出错时返回 `nil`。

在调用处，可以通过解包 optional 判断是否发生了问题：

```
if let myData = keychainData(service: "My Service") {
  do something with myData...
} else {
  fatalError("Something went wrong with... something?")
}
```

## 引入 Result

上面的方式有一种二元的优雅，但它隐藏着致命弱点。[从本质上说](https://github.com/apple/swift/blob/swift-5.0-RELEASE/stdlib/public/core/Optional.swift#L122)，`Optional` 只是一个枚举，包含某个被包装的值或什么也没有：

```
enum Optional<Wrapped> {
  case some(Wrapped)
  case none
}
```

当一切顺利时，这对我们的小工具完全足够，只需返回值即可。但多数涉及 I/O 的操作都可能失败（尤其是 `SecItemCopyMatching`，可能以[很多很多种方式](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes)失败），而 `Optional` 让我们无法表达某处出了问题。唯一能做的就是不返回任何东西。

与此同时，调用处想知道问题是什么，手中却只有空的 `.none`。当每种非理想状况本质上都被化约为 `¯\_(ツ)_/¯` 时，很难写出健壮的软件。怎样改善这一点？

一种做法是增加语言级特性，让函数除返回值外还能抛出错误。Swift 的确在第 2 版中通过 `throws/throw` 和 `do/catch` 语法做到了这一点。

不过先沿着 `Optional` 的思路继续想一下。若问题在于 `Optional` 只能保存一个值或 `nil`，而错误发生时 `nil` 的表达能力不足，也许只要创建一种能保存值 _或错误_ 的新 `Optional` 就能解决问题？

那么，恭喜你：改几个名称，我们会发现自己刚刚发明了新的 `Result` 类型，[它现已存在于 Swift 5 标准库中](https://github.com/apple/swift/blob/swift-5.0-RELEASE/stdlib/public/core/Result.swift#L16)！

```
enum Result<Success, Failure: Error> {
  case success(Success)
  case failure(Failure)
}
```

`Result` 保存成功值 _或_ 错误。我们可以用它改进这个小小的 Keychain 工具。

首先，定义一个自定义 `Error` 类型，其中包含比简单 `nil` 更具描述性的 case：

```
enum KeychainError: Error {
  case notData
  case notFound(name: String)
  case ioWentBad
  …
}
```

接着，将 `keychainData` 的定义从返回 `Data?` 改为返回 `Result<Data, Error>`。一切顺利时，我们将数据作为 `.success` 的[关联值](https://docs.swift.org/swift-book/LanguageGuide/Enumerations.html#ID148)返回。若 `SecItemCopyMatching` 众多且多变的灾难之一发生了呢？不再返回 `nil`，而是返回包装在 `.failure` 中的特定错误：

```
func keychainData(service: String) -> Result<Data, Error> {
  let query: NSDictionary = [...]
  var ref: CFTypeRef? = nil

  switch SecItemCopyMatching(query, &ref) {
  case errSecSuccess:
    guard let data = ref as? Data else {
      return .failure(KeychainError.notData)
    }
    return .success(data)
  case errSecItemNotFound:
    return .failure(KeychainError.notFound(name: service))
  case errSecIO:
    return .failure(KeychainError.ioWentBad)
  …
  }
}
```

现在，调用处能使用的信息多得多！如果愿意，可以对结果执行 `switch`，分别处理成功和每一种错误 case：

```
switch keychainData(service: "My Service") {
case .success(let data):
  do something with data...
case .failure(KeychainError.notFound(let name)):
  print("\(name) not found in keychain.")
case .failure(KeychainError.ioWentBad):
  print("Error reading from the keychain.")
case .failure(KeychainError.notData):
  print("Keychain is broken.")
…
}
```

综合来看，`Result` 似乎是对 `Optional` 很有用的升级。它为何花了五年才加入标准库？

## 三个就拥挤了

遗憾的是，`Result` _也_ 有致命弱点。此前我们只处理过对单个函数的一次调用，尚未注意到它；但设想一下，将两个容易出错的操作也加入返回 `Result` 的实用函数列表：

```
func makeAvatar(from user: Data) -> Result<UIImage, Error> {
  Return avatar made from user's initials...
  or return failure...
}

func save(image: UIImage) -> Result<Void, Error> {
  Save image and return success...
  or returns failure...
}
```

在这个示例中，第一个函数从用户数据生成头像，第二个函数将图像写入磁盘。实现细节对当前讨论不重要，关键在于它们都返回 `Result` 类型。

现在，该怎样编写一个操作：从 Keychain 取回用户数据，用它创建头像，将头像存盘，_并且_处理沿途可能发生的任何错误？

可能会尝试这样写：

```
switch keychainData(service: "UserData") {
case .success(let userData):

  switch makeAvatar(from: userData) {
  case .success(let avatar):

    switch save(image: avatar) {
    case .success:
      break // continue on with our program...

    case .failure(FileSystemError.readOnly):
      print("Can't write to disk.")

    …
    }

  case .failure(AvatarError.invalidUserFormat):
    print("Unable to generate avatar from given user.")

  …
  }

case .failure(KeychainError.notFound(let name)):
  print(""\(name)" not found in keychain.")

…
}
```

但天哪。仅增加两个函数，就带来了嵌套爆炸、分散的错误处理和痛苦。

## 无法展开

幸好，可以利用 `Result` 和 `Optional` 一样实现了 [`flatMap`](https://github.com/apple/swift/blob/swift-5.0-RELEASE/stdlib/public/core/Result.swift#L96) 这一点来清理代码。具体来说，对 `Result` 调用 `flatMap` 时，若为 `.success`，它会对关联值应用给定转换，并返回新生成的 `Result`；若为 `.failure`，`flatMap` 则不做修改地传递 `.failure` 及其关联错误。

由于它会如此传递错误，我们可以使用 `flatMap` 组合操作，而不必在每一步检查 `.failure`。这样能最小化嵌套，并让错误处理和操作本身保持分离：

```
let result = keychainData(service: "UserData")
             .flatMap(makeAvatar)
             .flatMap(save)

switch result {
case .success:
  break // continue on with our program...

case .failure(KeychainError.notFound(let name)):
  print(""\(name)" not found in keychain.")
case .failure(AvatarError.invalidUserFormat):
  print("Unable to generate avatar from given user.")
case .failure(FileSystemError.readOnly):
  print("Can't write to disk.")
…
}
```

这无疑是改进，不过它要求我们（以及阅读代码的任何人）足够熟悉 `.flatMap`，才能跟上它不太直观的语义。

将它与先前提到、Swift 2 就有的 `do/catch` 语法比较一下：

```
do {
  let userData = try keychainData(service: "UserData")
  let avatar = try makeAvatar(from: userData)
  try save(image: avatar)

} catch KeychainError.notFound(let name) {
  print(""\(name)" not found in keychain.")

} catch AvatarError.invalidUserFormat {
  print("Not enough memory to create avatar.")

} catch FileSystemError.readOnly {
  print("Could not save avatar to read-only media.")
} …
```

首先会注意到，这两段代码非常相似。它们上半部分都执行操作，下半部分都匹配并处理错误。

`Result` 版本通过链式调用 `flatMap` 传递操作；而 `do/catch` 代码的写法基本等同于没有任何错误处理。`Result` 版本要求理解其枚举内部结构，并显式对它执行 `switch` 以匹配错误；`do/catch` 版本则让我们聚焦真正关心的部分：错误本身。

有了语言级的错误处理语法，Swift 实际上屏蔽了本文前半部分刚消化的所有 `Result` 相关复杂性：枚举、关联值、泛型、flatMap、单子……某种意义上，Swift 在第 2 版增加错误处理语法，就是为了不必面对 `Result` 及其怪癖。

但五年后，我们却在学习它。为什么现在要加入它？

## 错误的起伏

碰巧，`do/catch` 有一个小小的致命弱点……

你看，`throw` 和 `return` 一样，只能向一个方向工作：向上。我们可以向 _调用方_ “向上” `throw` 错误，却不能把错误作为参数“向下” `throw` 给我们 _所调用的_ 另一个函数。

这种只能“向上”的行为通常正是我们想要的。再次用错误处理重写的 Keychain 工具中，只有 `return` 和 `throw`，因为它唯一职责就是将数据或错误向上交还给调用它的对象：

```
func keychainData(service: String) throws -> Data {
  let query: NSDictionary = [...]
  var ref: CFTypeRef? = nil

  switch SecItemCopyMatching(query, &ref) {
  case errSecSuccess:
    guard let data = ref as? Data else {
      throw KeychainError.notData
    }
    return data
  case errSecItemNotFound:
    throw KeychainError.notFound(name: service)
  case errSecIO:
    throw KeychainError.ioWentBad
  …
  }
}
```

但如果我们不从 Keychain 获取用户数据，而想从云服务获取呢？即便连接快速可靠，通过网络加载数据相较从磁盘读取仍可能耗时很久。当然不想等待时阻塞应用的其他部分，因此会让它异步执行。

但这意味着不再“向上”返回 _任何内容_，而是在完成时“向下”调用一个 closure：

```
func userData(for userID: String, completion: (Data) -> Void) {
  get data from the network
  // Then, sometime later:
  completion(myData)
}
```

现在网络操作可能以[各种不同错误](https://developer.apple.com/documentation/foundation/urlerror)失败，但无法“向下” `throw` 到 `completion` 中。因此，次优做法是将任何错误作为第二个（optional）参数传递：

```
func userData(for userID: String, completion: (Data?, Error?) -> Void) {
  Fetch data over the network...
  guard myError == nil else {
    completion(nil, myError)
  }
  completion(myData, nil)
}
```

但现在，调用者为了理解这个参数可能组合形成的笛卡尔迷宫，除真正关心的情形外，还必须处理许多不可能的情形：

```
userData(for: "jemmons") { maybeData, maybeError in
  switch (maybeData, maybeError) {
  case let (data?, nil):
    do something with data...
  case (nil, URLError.timedOut?):
    print("Connection timed out.")
  case (nil, nil):
    fatalError("🤔Hmm. This should never happen.")
  case (_?, _?):
    fatalError("😱What would this even mean?")
  …
  }
}
```

若能不再面对“数据或 nil _并且_错误或 nil”的混合体，而是有一种简洁方式仅表达“数据 _或_ 错误”，就太有帮助了。

## 别告诉我你听过这个

等等，数据或错误？听起来很熟悉。要是使用 `Result` 呢？

```
func userData(for userID: String, completion: (Result<Data, Error>) -> Void) {
  // Everything went well:
  completion(.success(myData))

  // Something went wrong:
  completion(.failure(myError))
}
```

调用处则是：

```
userData(for: "jemmons") { result in
  switch (result) {
  case (.success(let data)):
    do something with data...
  case (.failure(URLError.timedOut)):
    print("Connection timed out.")
  …
}
```

啊哈！由此可见，`Result` 类型可以作为 Swift 抽象概念 _“函数被标为 `throws` 时返回的那个东西”_ 的具体[实体化](https://en.wikipedia.org/wiki/Reification_%28computer_science%29)。因此，它可用于处理异步操作，因为异步操作要求传给完成处理程序的参数具有具体类型。

因此，尽管从 Swift 2 开始错误处理已暗示 `Result` 的形态（事实上，许多开发者在这些年间[创建了自己的版本](https://github.com/search?o=desc&q=result+language%3Aswift&s=&type=Repositories)），它如今才在 Swift 5 中正式加入标准库，主要用于处理异步错误。

这无疑优于前面看到的双 optional `(Value?, Error?)` 混乱。但我们刚才不是已经论证过，处理多个可能出错的调用时，`Result` 往往过于冗长、嵌套且复杂吗？确实如此。

而在 async 场景中问题更严重，因为 `flatMap` 预期其转换 _同步_ 返回。因此，无法用它组合 _异步_ 操作：

```
userData(for: "jemmons") { userResult in
  switch userResult {
  case .success(let user):
    fetchAvatar(for: user) { avatarResult in

      switch avatarResult {
      case .success(let avatar):
        cloudSave(image: avatar) { saveResult in

          switch saveResult {
          case .success:
            // All done!

          case .failure(URLError.timedOut)
            print("Operation timed out.")
          …
        }
      }

      case .failure(AvatarError.invalidUserFormat):
        print("User not recognized.")
      …
    }
  }

  case .failure(URLError.notConnectedToInternet):
    print("No internet detected.")
  …
}
```

## 等待未来

短期内，只能先接受它。它比语言原生的其他替代方案更好，而且异步调用的链式组合也不像同步调用那样常见。

但在未来，正如 Swift 用 `do/catch` 语法消除了同步错误处理中的 `Result` 嵌套问题一样，人们正考虑许多提案，以同样方式处理异步错误（以及更广义的异步处理）。

[async/await 提案](https://gist.github.com/lattner/429b9070918248274f25b714dcfc7619)就是其中之一。若被采纳，上面的代码将简化为：

```
do {
  let user = try await userData(for: "jemmons")
  let avatar = try await fetchAvatar(for: user)
  try await cloudSave(image: avatar)

} catch AvatarError.invalidUserFormat {
  print("User not recognized.")

} catch URLError.timedOut {
  print("Operation timed out.")

} catch URLError.notConnectedToInternet {
    print("No internet detected.")
} …
```

天哪！尽管我喜爱 `Result`，但我个人迫不及待想看到它被光荣的 async/await 霸主彻底变得无关紧要。

与此同时，欢呼吧！标准库终于有了具体的 `Result` 类型，照亮这段 async 错误处理的中世纪。
