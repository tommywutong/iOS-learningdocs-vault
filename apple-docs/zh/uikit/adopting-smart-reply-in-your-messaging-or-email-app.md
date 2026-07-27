---
title: 在信息或邮件 App 中采用智能回复
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app
source_url: 'https://developer.apple.com/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/adopting-smart-reply-in-your-messaging-or-email-app.json'
content_hash: 'sha256:d8a44fa4a9328e92'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [Keyboards and input](keyboards-and-input.md)

# 在信息或邮件 App 中采用智能回复

<sub>文章</sub>

使用 Apple 智能生成回复建议，并将所选文本放入文本 UI。

## 概述

“信息”和“邮件”使用 Apple 智能提供“智能回复”功能。当你撰写信息或电子邮件时，该功能会生成与会话上下文相关的建议。要将此功能添加到你的信息或邮件 App，请执行以下步骤：

- 使用 App 中某个会话的数据创建_对话上下文_对象。
- 准备用户界面时，将对话上下文附加到文本视图或文本字段。
- 实现委托（delegate）方法，以便在发送或接收信息时让对话上下文保持最新。
- 对于电子邮件或其他长篇信息类型，使用所选输入建议生成长篇回复，并将其放入输入字段。

### 创建对话上下文

为了向 Apple 智能提供生成智能回复所需的上下文，请使用信息对话的相关信息创建对话上下文对象。此对象包括对话参与者的信息和对话中的文本条目。

准备用户界面以便与一名或多名参与者收发信息时，请创建能反映 App 中信息会话类型的对话上下文：信息使用 [UIMessageConversationContext](uimessageconversationcontext.md)，电子邮件使用 [UIMailConversationContext](uimailconversationcontext.md)。

使用以下详细信息配置对话上下文：

- 会话的唯一标识符
- 会话参与者的唯一标识符和姓名字典
- 当前使用你的 App 收发信息的用户标识符集合
- 对话中其他人的标识符集合
- 与会话类型相应的对话条目数组，即 [MessageEntry](uimessageconversationcontext/messageentry.md) 或 [MailEntry](uimailconversationcontext/mailentry.md)

以下展示如何配置对话上下文：

**Swift**

```swift
func mailConversationContext(for yourEntries: [YourMailEntry]) -> UIMailConversationContext {
    var context: UIMailConversationContext = UIMailConversationContext()

    var contextEntries: [UIMailConversationContext.MailEntry] = []
    for yourEntry in yourEntries {
        var conversationEntry = UIMailConversationContext.MailEntry()

        conversationEntry.text = yourEntry.text
        conversationEntry.senderIdentifier = yourEntry.sender
        conversationEntry.primaryRecipientIdentifiers = [yourEntry.recipient]
        conversationEntry.sentDate = yourEntry.date
        conversationEntry.entryIdentifier = yourEntry.yourEntryIdentifier
        conversationEntry.kind = .personal

        contextEntries.append(conversationEntry)
    }

    context.threadIdentifier = yourThreadObject.identifier
    context.entries = contextEntries

    var senderName = PersonNameComponents()
    senderName.givenName = "Sender's name"

    var recipientName = PersonNameComponents()
    recipientName.givenName = "Recipient's name"

    context.participantNameByIdentifier = [senderIdentifier: senderName, recipientIdentifier: recipientName]

    context.selfIdentifiers = [senderIdentifier]

    context.responsePrimaryRecipientIdentifiers = [recipientIdentifier]

    return context
}
```

**Objective-C**

```objc
- (UIMailConversationContext *)mailConversationContextForEntries:(NSArray<YourMailEntry *> *)yourEntries {
    UIMailConversationContext *context = [[UIMailConversationContext alloc] init];

    NSMutableArray *contextEntries = [NSMutableArray new];
    for (YourMailEntry *yourEntry in yourEntries) {
        UIMailConversationEntry *conversationEntry = [[UIMailConversationEntry alloc] init];
        conversationEntry.text = yourEntry.text;
        conversationEntry.senderIdentifier = yourEntry.sender;

        conversationEntry.primaryRecipientIdentifiers = [NSSet setWithObject:yourEntry.recipient];

        conversationEntry.sentDate = yourEntry.date;
        conversationEntry.entryIdentifier = yourEntry.yourEntryIdentifier;

        conversationEntry.kind = UIMailConversationEntryKindPersonal;

        [contextEntries addObject:conversationEntry];
    }

    context.threadIdentifier = yourThreadObject.identifier;
    context.entries = contextEntries;

    NSPersonNameComponents *senderName = [[NSPersonNameComponents alloc] init];
    senderName.givenName = @"Sender's name";

    NSPersonNameComponents *recipientName = [[NSPersonNameComponents alloc] init];
    recipientName.givenName = @"Recipient's name";

    context.participantNameByIdentifier = @{
        senderID : senderName,
        recipientID : recipientName
    };

    context.selfIdentifiers = [NSSet setWithObject:senderID];

    context.responsePrimaryRecipientIdentifiers = [NSSet setWithArray:@[recipientID]];

    return context;
}
```

### 将对话上下文附加到文本视图或文本字段

创建文本视图或文本字段等输入字段以获取 App 用户的输入时，请在键盘出现之前，将所创建的对话上下文赋给该对象的 [conversationContext](uitextinputtraits/conversationcontext.md) 属性：

**Swift**

```swift
entryField.conversationContext = context
```

**Objective-C**

```objc
[self.entryField setConversationContext:context];
```

键盘会在每个会话中使用此上下文一次来进行初始化。请按照下一节中的步骤处理键盘会话期间对话发生的变化。

### 让对话上下文保持最新

每次发送或接收信息时，都要让对话上下文保持最新。由于对话上下文与键盘会话绑定，如果焦点已离开输入字段，请更新或重新生成先前创建的对话上下文，然后将输入字段的 `conversationContext` 设为更新后的上下文：

**Swift**

```swift
entryField.conversationContext = context
```

**Objective-C**

```objc
[self.entryField setConversationContext:context];
```

然后，在输入字段的 `inputDelegate` 上调用 [- conversationContext:didChange:](<uitextinputdelegate/conversationcontext(__didchange_).md>)，通知它对话中增加了条目：

**Swift**

```swift
entryField.inputDelegate?.conversationContext(context, didChange: entryField)
```

**Objective-C**

```objc
id<UITextInputDelegate> entryFieldInputDelegate = (id<UITextInputDelegate>)self.entryField.inputDelegate;

[entryFieldInputDelegate conversationContext:context didChange:self.entryField];
```

### 生成长篇回复

对于电子邮件或其他长篇信息 App，不要直接将智能回复的响应放入输入字段，而是使用该建议通过你自己的模型生成长篇回复。为此，请实现 [- textView:insertInputSuggestion:](<uitextviewdelegate/textview(__insertinputsuggestion_).md>) 或 [- textField:insertInputSuggestion:](<uitextfielddelegate/textfield(__insertinputsuggestion_).md>)：

**Swift**

```swift
func textField(_:UITextField, insertInputSuggestion inputSuggestion: UIInputSuggestion) {
    guard let smartReplySuggestion = inputSuggestion as? UISmartReplySuggestion else {
        return
    }

    // 使用 smartReplySuggestion.smartReply 调用你的模型，
    // 然后将结果赋给输入字段的 text 属性。
    let entryFieldText = YourModel.response(from: smartReplySuggestion.smartReply)
    entryField.text = entryFieldText
}
```

**Objective-C**

```objc
- (void)textField:(UITextField *)textField insertInputSuggestion:(UIInputSuggestion *)inputSuggestion {
    if ([inputSuggestion.class isEqual:UISmartReplySuggestion.class]) {
        UISmartReplySuggestion *smartReplySuggestion = (UISmartReplySuggestion *)inputSuggestion;

        // 使用 smartReplySuggestion.smartReply 调用你的模型，
        // 然后将结果赋给输入字段的 text 属性。
        NSString *entryFieldText = [YourModel responseFrom:smartReplySuggestion.smartReply];

        self.entryField.text = entryFieldText;
    }
}
```

如果输入字段是 [UITextInput](uitextinput.md) 的自定义实现，请改为调用 [- insertInputSuggestion:](<uitextinput/insert(__).md>)。

### 了解系统何时生成智能回复建议

系统仅在特定情况下生成智能回复建议，并且可能不会在所有情况下都生成建议。

信息对话可以生成建议的情况包括：

- 输入字段为空。
- 对话中的最后一条信息来自接收者，而不是发送信息的人。
- 对话中之前的信息是文本，而不是图像或表情符号。
- 之前的信息是近期发送的。

邮件对话可以生成建议的情况包括：

- 用户是电子邮件的直接接收者，而不在抄送或密送列表中。
- 用户尚未回复该电子邮件。
- 电子邮件的发送者和接收者使用不同的电子邮件地址。

## 另请参阅

### 信息的智能回复

- [UIConversationContext](uiconversationcontext.md) — 表示参与者之间对话的基类，例如邮件或信息 App 中的对话。
- [Entry](uiconversationcontext/entry.md) — 表示对话中一条信息的基类。
- [UIMailConversationContext](uimailconversationcontext.md) — 表示电子邮件对话的类。
- [MailEntry](uimailconversationcontext/mailentry.md) — 表示电子邮件会话中特定邮件的类。
- [UIMessageConversationContext](uimessageconversationcontext.md) — 表示信息对话的类。
- [MessageEntry](uimessageconversationcontext/messageentry.md) — 表示信息对话中一条信息的类。
- [UIInputSuggestion](uiinputsuggestion.md) — 用于处理来自键盘或系统建议的基类。
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md) — 携带人物、主题、位置和时间段照片搜索元数据的输入建议。_（Beta）_
- [UISmartReplySuggestion](uismartreplysuggestion.md) — 用于处理智能回复建议的类。
