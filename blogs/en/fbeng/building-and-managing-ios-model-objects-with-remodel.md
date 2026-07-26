---
title: Building and managing iOS model objects with Remodel
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2016/04/13/ios/building-and-managing-ios-model-objects-with-remodel/'
original_language: en
published: 2016-04-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0602665ba49cbc25'
translated: false
---

> 原文：[Building and managing iOS model objects with Remodel](https://engineering.fb.com/2016/04/13/ios/building-and-managing-ios-model-objects-with-remodel/)　·　Meta Engineering — iOS

One of the aspects of building an application is deciding how data will flow through it. Many iOS developers use dictionaries for this purpose, or use handwritten, simple objects instead. We've seen these patterns in our use of Objective-C at Facebook, and we've found some drawbacks in these approaches. Passing dictionaries of data around proved dangerous because dictionary fields are not type-safe. We also found that maintaining custom model objects was time-consuming, tedious, and error-prone.

To solve these problems, we built Remodel, an Objective-C code generation tool specialized for quickly creating and editing model objects.

As our codebase scaled, we found that giving these objects certain properties enforced good patterns (such as the separation of data and behavior), enabled a simpler programming model, allowed us to explore lock-free multi-threading strategies, and simplified unit test writing.

Today, we're excited to announce that we are open-sourcing [Remodel](https://github.com/facebook/remodel). In addition to introducing the fundamentals of Remodel, this post will cover the architectural benefits of building a system with immutable value models.

## Remodel basics

Say you have an app that shows users, which receives a JSON response that looks like:

```clike
// User
{
  'id': 30,
  'nickname': '@messageAppUser1',
  'imageUrl': 'http://cdn.fb.com/y93kdo4d4r'
}
```

Once data like this winds up in the network layer, you're going to have to figure out how to pass it around to other parts of the system. One option would be a dictionary like this:

```clike
@{
   @'id': @(30),
   @'nickname': @'@messageAppUser1',
   @'imageUrl': 'http://cdn.fb.com/y93kdo4d4r'
 }
```

If you take this approach, you'll quickly run into type safety issues — the compiler won't help you be sure that, for example, a dictionary passed into your method would contain the entries you're expecting or that they're the right type. If someone decided to pass an NSNumber as the nickname value, the compiler would successfully build your application, yet a crash would be likely when your app is run. Relying on the compiler is an important part of working in iOS, and the benefits of compile-time errors over runtime errors should not be disregarded.

One way to avoid the drawbacks of the dictionary approach is to write your own class for the data. This addresses most of the concerns, in that you can now have strong typing around your data and feel more comfortable passing it around your application. For User, this class might look something like the following:

```clike
@interface User : NSObject
@property (nonatomic) NSUInteger userId;
@property (nonatomic) NSString *nickname;
@property (nonatomic) NSURL *imageUrl;
    @end
```

This seems workable, but soon enough you'll find that there other things you'd like to do with the object. For example, when you log this object, you'll get a message that doesn't show the object's contents, which can be useful when debugging:

```clike
> <User: 0x7f9b8340ca20>
```

Getting a message that is more useful for debugging requires writing a description method:

```clike
- (NSString *)description
{
  return [NSString stringWithFormat:@"%@ - \n\t userId: %tu; \n\t nickname: %@; \n\t imageUrl: %@; \n", [super description], _userId, _nickname, _imageUrl];
}
    // now the output would read:
> <User: 0x7fdfb51000f0> - 
userId: 30; 
nickname: @messageAppUser1; 
imageUrl: http://cdn.fb.com/y93kdo4d4r;
```

If you want to cache this data locally to avoid refetching it from the server, you'll have to write the ability to code/decode the object. For example:

```clike
- (void)encodeWithCoder:(NSCoder *)aCoder
{
  [aCoder encodeInteger:_userId forKey:@"userIdKey"];
  [aCoder encodeObject:_nickname forKey:@"nicknameKey"];
  [aCoder encodeObject:_imageUrl forKey:@"imageUrlKey"];
}
```

Without careful treatment, these methods can easily run into problems, like trying to restore the wrong value for a given key. Since ` decodeObjectForKey` simply returns an object of type `id`, it's very possible to wind up with an object of the wrong type, which could cause a crash down the line.

Often, you’ll also want your data to be immutable so that you can pass it around with the confidence that no other objects will change it (more on that later). To do this, you'll have to label the properties readonly and pass the values into an initializer:

```clike
@interface User : NSObject
@property (nonatomic, readonly) NSUInteger userId;
@property (nonatomic, readonly) NSString *nickname;
@property (nonatomic, readonly) NSURL *imageUrl;

- (instancetype)initWithUserId:(NSUInteger)userId
                      nickname:(NSString *)nickname
                      imageUrl:(NSURL *)imageUrl;

    @end
```

At this point, you will have referenced each attribute seven times (twice in the header, twice in initializer implementation, once in encode, once in decode, and once in description). That's a lot of boilerplate. Boilerplate isn't just annoying, it's dangerous. Tedious tasks tend to be done inattentively, and that's when mistakes are introduced.

This is where Remodel can really help. To use Remodel, define your data's schema in a simple format. When you run the Remodel script, it will use this information to generate an Objective-C object that has a description and coding.

This means that adding a property to a data object is truly a one-line change — no copy-paste required.

```clike
// Model definition
User {
  NSUInteger userId
  NSString *nickname
  NSURL *imageUrl
}

> remodel/bin/generateValues User.value

// Generated header for User.value
#import <Foundation/Foundation.h>

@interface User : NSObject <NSCoding>

@property (nonatomic, readonly) NSUInteger userId;
@property (nonatomic, readonly, copy) NSString *nickname;
@property (nonatomic, readonly, copy) NSURL *imageUrl;

- (instancetype)initWithUserId:(NSUInteger)userId nickname:(NSString *)nickname imageUrl:(NSURL *)imageUrl;

@end
  

// Generated implementation for User.value
#import "User.h"

static __unsafe_unretained NSString * const kUserIdKey = @"USER_ID";
static __unsafe_unretained NSString * const kNicknameKey = @"NICKNAME";
static __unsafe_unretained NSString * const kImageUrlKey = @"IMAGE_URL";

@implementation User

- (instancetype)initWithCoder:(NSCoder *)aDecoder
{
  if ((self = [super init])) {
    _userId = [aDecoder decodeIntegerForKey:kUserIdKey];
    _nickname = [aDecoder decodeObjectForKey:kNicknameKey];
    _imageUrl = [aDecoder decodeObjectForKey:kImageUrlKey];
  }
  return self;
}

- (instancetype)initWithUserId:(NSUInteger)userId nickname:(NSString *)nickname imageUrl:(NSURL *)imageUrl
{
  if ((self = [super init])) {
    _userId = userId;
    _nickname = [nickname copy];
    _imageUrl = [imageUrl copy];
  }

  return self;
}

- (NSString *)description
{
  return [NSString stringWithFormat:@"%@ - \n\t userId: %tu; \n\t nickname: %@; \n\t imageUrl: %@; \n", [super description], _userId, _nickname, _imageUrl];
}

- (void)encodeWithCoder:(NSCoder *)aCoder
{
  [aCoder encodeInteger:_userId forKey:kUserIdKey];
  [aCoder encodeObject:_nickname forKey:kNicknameKey];
  [aCoder encodeObject:_imageUrl forKey:kImageUrlKey];
}

@end
```

## Modeling your architecture

As we've seen, Remodel is great for generating repetitive code that would otherwise have to be written by hand.

In order to fully appreciate Remodel, however, we need to understand the architectural benefits of building a system using the type of objects Remodel generates by default: immutable value models. We'll do this by examining what benefit each element in the name “immutable value model” brings.

For the purposes of this discussion, we'll consider a simple messaging app.

### Why simple models?

Any app or library is composed of state and behavior. One of the pitfalls of common object-oriented design is that state and behavior are often mixed on the same object. For example, consider the following `Conversation` object:

```clike
@interface Conversation : NSObject
@property (nonatomic, readonly) NSArray<User *> *participants;
@property (nonatomic, readonly) NSArray<Messages *> *messages;
// sends this message over the network and updates the messages collection.
- (void)sendMessage:(Message *)message completeBlock:(MessageSendCompleteBlock)completeBlock;
    @end
```

When an object is doing a complex operation like sending, it's going to want to track some internal state. For example, the Conversation probably needs to keep track of which messages are currently being sent and how the network request is going. Ideally, the Conversation object would not expose this state, because it creates unnecessary clutter. Furthermore, if it is mutable, exposing this state would also make it hard to understand how the send process is managed. Given this, the implementation of Conversation might look like:

```clike
@implemenation Conversation {
  Message *_currentlySendingMessage;
  NSOperation *_sendOperation;
}
...
    @end
```

This plan seems OK, but you might have other objects that want to keep similar bookkeeping around sending, such as the Message object:

```clike
@interface Message : NSObject
@property (nonatomic, readonly) BOOL isSending;
.... 
// sends this message over network and 
- (void)sendToConversation:(Conversation *)conversation completeBlock:(MessageSendCompleteBlock)completeBlock;
@end

@implementation Message {
  NSDate *sendTimestamp; 
}
 
@end
```

This seems reasonable, except now, to a reader, it's not clear if the method on `Message` is what's actually doing the send, if the `Conversation` is doing the sending, or if both objects are.

This type of confusion makes code harder to reason about and, as a result, tends to lead to monolithic designs, in which one object does most things.

```clike
@interface Conversation : NSObject
// Core message sending
- (void)sendMessage:(Message *)message;
- (void)markMessageAsRead:(Message *)message;
- (void)markMessageAsUnread:(Message *)message;

// Participant
- (void)addParticipant:(User *)user;
- (void)removePariticipant:(User *)user;

// Customization info
- (void)addThreadCoverPhoto:(Photo *)photo;
- (void)addThreadName:(NSString *)name;
// ...and so on
    @end
```

Separating state from behavior is a good start for breaking up objects like `Conversation`.

In this example, that would mean representing our state as simple models while writing single-purpose classes that perform the operations. This helps your app scale because many developers can work on separate parts of the same project while avoiding conflicts with other work that's happening in tandem. For example, in the proposed system below, the person who works on sending can operate in an entirely different file than the person who's building the thread-management methods.

```clike
@interface Conversation : NSObject
@property (nonatomic) NSArray<User *> *participants;
@property (nonatomic) NSArray<Message *> *messages;
@property (nonatomic) NSString *threadName;
@property (nonatomic) Photo *coverPhoto;
@end

@interface MessageSender : NSObject
// Sends a message over the network and applies the appropriate updates to the 
// Message and Conversation objects supplied.
- (void)sendMessage:(Message *)message toConversation:(Conversation *)conversation;
@end

@interface ConversationCustomizer : NSObject
// Updates the photo and the thread's timestamp. Also, adds an admin message to the conversation noting the update
- (void)setCoverPhoto:(Photo *)photo forConversation:(Conversation *)conversation withActor:(User *)actor;
- (void)setName:(NSString *)name forConversation:(Conversation *)conversation withActor:(User *)actor;
    @end
```

### Immutability

So now that you're building simple model objects, let's take a second to consider how your model objects should work. Here is a naive version of the Conversation model object from step 2:

```clike
@interface Conversation : NSObject
@property (nonatomic) NSArray<User *> *participants;
@property (nonatomic) NSArray<Message *> *messages;
@property (nonatomic) NSString *threadName;
@property (nonatomic) Photo *coverPhoto;
    @end
```

Looking at the system as a whole, it becomes apparent that reasoning about where changes are happening to a model will become intractable.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GDz6twDNBpQ9PbEAAA2xXxYAAAAAbj0JAAAB.jpg)

Once you begin thinking about multi-threading, the complexity can spiral out of control because of issues like race conditions. A simple approach to multi-threading here might be to synchronize our getters/setters. Problem solved!

```clike
@interface Conversation : NSObject
@property (atomic) NSArra<User *> *participants;
@property (atomic) NSArray<Message *> *messages;
@property (atomic) NSString *threadName;
@property (atomic) Photo *coverPhoto;
    @end
```

It turns out that this isn't a full solution: Certain complex operations can't be easily modeled in this system, such as an operation that requires an atomic get and set.

```clike
- (void)sendMessage:(Message *)message toConversation:(Conversation *)conversation
{
   NSMutableArray<Message *> *messagesMutable = [conversation.messages mutableCopy];
   [messagesMutable addObject:message];
   // Hope that no one updated this conversation's messages after we read it
   conversation.messages = messagesMutable;
    }
```

Another danger of working with mutable data is not keeping object observers up to date.

Consider a simplified view controller:

```clike
@implementation MessagesViewController {
  Conversation *_conversation;
}

...

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return _conversation.messages.count;
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
{
  MessageCell *cell = [tableView dequeueReusableCellWithIdentifier:@"MessageCell"];
  if (cell == nil) {
    cell = [[MessageCell alloc] initWithStyle:UITableViewCellStyleSubtitle reuseIdentifier:@"MessageCell"];
  }

  [cell configureWithMessage:_conversation.messages[indexPath.row]]

  return cell;
}

    @end
```

The code in the above example seems safe, but with mutable models, it is actually quite dangerous. If we forget to reload data when the messages on the conversation change — which can occur anywhere in your code due the mutable model — the app could crash with a NSInternalInconsistencyException in our UITableView. Another possibility is that your app could crash with an out-of-bounds exception in the case of a delete, or the app could show inconsistent data.

The above scenarios can produce bugs that are very difficult to solve, as fixing them will require tracking down the component that caused the update and ensuring that your TableViewController is ready for the update when it comes.

A different approach here can mitigate these problems. If disparate objects are not allowed to mutate your representation of a conversation, it becomes easier to see how data is flowing through your system. By centralizing the update path, you no longer have to worry about tracking each component that's editing your data.

When paired with Apple's Grand Central Dispatch (GCD) framework, the update system can run on a single background queue, will be easier to manage, and will scale to multiple engineers working in the system.

![](https://engineering.fb.com/wp-content/uploads/2016/04/GOlLxgDtUgOUHTcHAFna0X8AAAAAbj0JAAAB.jpg)

Now the code might look more like the following:

```clike
@interface Conversation : NSObject

@property (nonatomic, readonly) NSArray<User *> *participants;
@property (nonatomic, readonly) NSArray<Message *> *messages;
@property (nonatomic, readonly) NSString *threadName;
@property (nonatomic, readonly) Photo *coverPhoto;

- (instancetype)initWithParticipants:(NSArray<User *> *)participants 
                            messages:(NSArray<Message *> *)messages
                          threadName:(NSString *)threadName
                          coverPhoto:(Photo *)coverPhoto;
@end

@protocol MessageUpdateListening
- (void)didUpdateConversation:(Conversation *)conversation;
@end

@interface MessageSender : NSObject

- (instancetype)initWithUpdateListener:(id<MessageUpdateListening>)listener;

// Sends a message to the specified conversation. Announces the updated model
// to the consuming listener
- (void)sendMessage:(Message *)message 
     toConversation:(NSString *)conversationId;
     
@end
```

### Value objects

In iOS, objects are normally compared by their pointers. However, in many situations it is convenient to compare models by their contents rather than by their identity.

For example, consider the case where a Conversation object passed into a method that needs to determine which specific subobject has changed:

```clike
- (void)didUpdateConversation:(Conversation *)conversation
{
    if (![conversation.messages isEqual:_conversation.messages]) {
      [self _updateMessages:conversation.messages];
    }
    
    if (![conversation.participants isEqual:_conversation.participants]) {
      [self _updateParticipants:conversation.participants];
    }
    
    _conversation = conversation;
}
```

Likewise, by being immutable and compared by value, your model objects can act as a key in an NSDictionary or as a value in an NSSet. Also, all immutable objects trivially implement NSCopying. So, with this insight, we now have:

```clike
@interface Conversation : NSObject<NSCopying>

@property (nonatomic, readonly) NSSet<User *> *participants;
@property (nonatomic, readonly) NSOrderedSet<Message *> *messages;

....

@end
```

If you've made it this far, then you should understand (and possibly have) the motivation to build lots of immutable value objects.

## Remodel deep dive

Now that we've covered the basics of Remodel and the architectural motivations for using it, let's dig a little deeper.

For the implementation of the Remodel tool itself, we chose TypeScript because we liked the fact that JavaScript is an extremely popular and well-known scripting language that's also suited toward functional programming. TypeScript uses JavaScript's familiar syntax but adds compile-time support for strong types and generics, filling in one of the major gaps in the language.

### Plugins

As we started generating our model objects, we realized that we could also use the field information in the `.value` file to generate other useful utilities. As previously mentioned, we built support for generating coding methods on our objects, which makes writing Remodel objects to a disk or transporting over network very easy.

That said, we knew that some of these features might not apply to all models. To solve this, we introduced the `includes` and `excludes` keywords, which let specific Remodel objects control what code will be generated for them:

```clike
%type name="Messages"
Conversation includes(RMBuilder) excludes(RMCoding) {
  NSSet<User *> *participants;
  NSOrderedSet<Message *> *messages;
  NSString *threadName;
  Photo *coverPhoto;
    }
```

The `excludes` here will cause us to not generate the coding portion of this object. Likewise, the `includes` will activate a feature that will create a "Builder" object in addition to the normal Remodel output.

For example:

```clike
#import <Foundation/Foundation.h>

@class Conversation;
@class Messages;
@class Photo;

@interface ConversationBuilder : NSObject

+ (instancetype)conversation;

+ (instancetype)conversationFromExistingConversation:(Conversation *)existingConversation;

- (Conversation *)build;

- (instancetype)withParticipants:(NSSet<User *> *)participants;

- (instancetype)withMessages:(NSOrderedSet<Message *> *)messages;

- (instancetype)withThreadName:(NSString *)threadName;

- (instancetype)withCoverPhoto:(Photo *)coverPhoto;

@end
```

Builder objects are particularly useful in two cases.

First, inside of your unit tests you generally want to specify only the minimum number of properties that the test depends on. With builders you can avoid directly calling the initializer, which means that you will not have to update every test when you decide to add a new property onto a value object.

Second, they make creating a new value object with only a subset of properties very easy.

These are a couple of examples of the types of features you can activate and deactivate by using plugins, but that's only the beginning of what you can do with them.

### Customizing Remodel

Under the covers, Remodel is a pretty generic Objective-C code generation tool, and it includes support for writing your own plugin objects. Adding your own plugins can be very powerful.

Plugins are written in (or compiled to) JavaScript and conform to a simple API (shown below in TypeScript). Consider the sample below, where we add a plugin that populates an NSDictionary from a Remodel object:

```clike
export function createPlugin():ValueObject.Plugin {
  return {
    ...
    additionalFiles: function(valueType:ValueObject.TypeInformation):Code.File[] {
      return [
        dictionaryCreatorFileForValueType(valueType)
      ];
    },
    ...
    requiredIncludesToRun: ['DictionaryCreator'],
    ...
  };
    }
```

Plugin methods can return new properties, fields, or, in this case, an entirely new file. Here is the method you'll use in this plugin to create our new file:

```clike
function dictionaryCreatorFileForValueType(valueTypeInfo:ValueObject.TypeInformation):Code.File {
  return {
    name: valueTypeInfo.typeName + 'DictionaryCreatorHelpers',
    type: Code.FileType.ObjectiveC(),
    imports:[
      {file:'Foundation.h', isPublic:true, library:Maybe.Just<string>('Foundation')},
      {file:valueTypeInfo.typeName + '.h', isPublic:true, library:Maybe.Nothing<string>()},
    ],
    enumerations: [],
    blockTypes: [],
    comments: [],
    forwardDeclarations: [],
    staticConstants: [],
    functions: [
      dictionaryCreatorFunctionDefinitionForValueType(valueTypeInfo)
    ],
    classes: [],
    diagnosticIgnores:[],
    namespaces: []
  };
    }
```

The plugin methods are also supplied with information about the specific Remodel definition they are working on (typed as `ValueObject.TypeInformation`). In this case, we will use that information to create a method definition and body:

```clike
// Create the signature for our NSDictionary create function.
function dictionaryCreatorFunctionDefinitionForValueType(valueTypeInfo:ValueObject.TypeInformation):ObjC.Function {
  var valueObjectParameterName = StringUtils.lowercased(valueTypeInfo.typeName);
  return {
    comments:[ { content: '// A function that statelessly creates an NSDictionary from  a ' + valueTypeInfo.typeName + 'object.' } ],
    name:valueTypeInfo.typeName + 'DictionaryCreator',
    parameters:[{ name:valueObjectParameterName,
                  type:{ name:valueTypeInfo.typeName, reference:valueTypeInfo.typeName + '*' }
                }],
    returnType:Maybe.Just({ name:'NSDictionary', reference:'NSDictionary *'}),
    code:dictionaryInflatorFunctionBodyForValueType(valueTypeInfo, valueObjectParameterName),
    isPublic:true,
  }
}

// Create the function body
function dictionaryCreatorFunctionBodyForValueType(valueTypeInfo:ValueObject.TypeInformation, valueObjectVariableName:string):string[] {
  var initializerLine = 'NSMutableDictionary *dict = [[NSMutableDictionary alloc] init];';

  var attributeLines = valueTypeInfo.attributes.map(
    function(attr:ValueObject.TypeInformationAttribute):string {
      var assignmentExpression = valueObjectVariableName + '.' + attr.name;
      return 'dict[@"' + attr.name + '"] = ' + valueObjectVariableName + '.' + attr.name + ';';
    });

  var returnLine = 'return [dict copy]';

  return [ initializerLine ].concat(attributeLines).concat(returnLine);
    }
```

When included by a .value file, your simple plugin will create a new file that has a method to generate a dictionary based on the contents of that value object.

So, now you just update your Remodel configuration, your value object, and rerun it through Remodel.

```clike
%type name="Messages"
Conversation includes(DictionaryCreator) {
  ...
}

// ConversationDictionaryCreatorHelpers.h

...
// A function that statelessly creates an NSDictionary from  a Conversationobject.
extern NSDictionary *ConversationDictionaryCreator(Conversation *conversation);
....

// ConversationDictionaryCreatorHelpers.m
extern NSDictionary *ConversationDictionaryCreator(Conversation *conversation) {
  NSMutableDictionary *dict = [[NSMutableDictionary alloc] init];
  dict[@"participants"] = conversation.participants;
  dict[@"messages"] = conversation.messages;
  dict[@"threadName"] = conversation.threadName;
  dict[@"coverPhoto"] = conversation.coverPhoto;
  return [dict copy]
    }
```

Note that this function isn't perfect — for example, one flaw is that it will not compile if your value object has non-pointer types in it. Remodel comes bundled with helpers for dealing with properties with different types, so it wouldn't be hard to add this support.

Still, it should show how easy it is to generate useful methods that update themselves automatically when the value object definition changes.

### Filling out your object hierarchy with abstract types

Once you have lots of models in your system, you'll naturally want to make expressive model hierarchies to represent the constraints of your data. Abstract objects are an important element in a system like this.

Specifically, consider the case where you have different types of message content: Photo, Sticker, and Text. A message's content can be exactly one of these three things. It's not easy to represent this in a .value object; you'd need to have something like:

```clike
MessageContent {
 ContentType(NSUInteger) type
 # Set if the type is ContentTypePhoto
 Photo *photo;
 # Set if the type is ContentTypeSticker
 NSInteger stickerId
 # Set if the type is ContentTypeText
 NSString *text
    }
```

The problem here is that if the object can be only one of these things, it's cumbersome to have to check the type before you read any property. It's also pretty easy to create invalid objects this way, and it's unclear how much validation consumers should do.

Algebraic data types (ADTs) can help solve this problem, and we built an ADT generator into Remodel. In this case, we would have an `.adtValue` file:

```clike
MessageContent includes(RMCoding) {
  image {
    Photo *photo
  }
  sticker {
    NSInteger stickerId
  }
  text {
     NSString *body
  }
}
```

Running Remodel on this file would yield the following Objective-C object:

```clike
#import <Foundation/Foundation.h>
#import "Photo.h"

typedef void (^MessageContentImageMatchHandler)(Photo *photo);
typedef void (^MessageContentStickerMatchHandler)(NSInteger stickerId);
typedef void (^MessageContentTextMatchHandler)(NSString *body);

@interface MessageContent : NSObject <NSCopying, NSCoding>

+ (instancetype)imageWithPhoto:(Photo *)photo;

+ (instancetype)stickerWithStickerId:(NSInteger)stickerId;

+ (instancetype)textWithBody:(NSString *)body;

- (void)matchImage:(MessageContentImageMatchHandler)imageMatchHandler sticker:(MessageContentStickerMatchHandler)stickerMatchHandler text:(MessageContentTextMatchHandler)textMatchHandler;

@end
```

To operate on a MessageContent object, we match it to figure out what type it is and extract its contents in one step. For example:

```clike
- (void)renderContent:(MessageContent *)content
{
  [content
   matchImage:^(Photo *photo) {
     [self _renderPhoto:photo];
   }
   sticker:^(NSInteger stickerId) {
     [self _renderSticker:stickerId];
   }
   text:^(NSString *body) {
    [self _renderText:body];
   }];
}
```

Now your Message object can simply be:

```clike
Message {
  NSInteger messageId
  MessageContent *content
  NSTimeInterval timestamp
    }
```

And if we fill out the object hierarchy, we'll get something that looks like:

![](https://engineering.fb.com/wp-content/uploads/2016/04/GPVLxgCanxjsmuECAAqJGlsAAAAAbj0JAAAB.jpg)

## Conclusion

Immutable value objects make great models for complex, scalable systems.

Remodel is a flexible tool for generating these objects and associated helpers in Objective-C. These objects are battle-tested in our Objective-C codebase at Facebook, representing the data of familiar parts of our app, such as the content of a status update, and we hope you find the Remodel tool and associated patterns useful as well.
