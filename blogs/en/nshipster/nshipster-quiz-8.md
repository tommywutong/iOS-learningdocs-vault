---
title: 'NSHipster Quiz #8'
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/nshipster-quiz-8/'
original_language: en
published: 2016-06-14
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:9873cb055c435147'
translated: false
---

> 原文：[NSHipster Quiz #8](https://nshipster.com/nshipster-quiz-8/)　·　NSHipster (Mattt)

# [NSHipster Quiz #8](https://nshipster.com/nshipster-quiz-8/)

Written by  [Nate Cook](https://nshipster.com/authors/nate-cook/)  June 14^th, 2016

This year’s WWDC edition of the NSHipster Pub Quiz was held on June 14th, once again testing the assembled developers with questions both random and obscure. We’re enormously grateful to [Realm](https://realm.io), who hosted the quiz for the second year in a row, with delicious food and drink and enough tables to seat nearly two hundred contestants.

Competition was as fierce as always. Laughs and groans were heard. And after the points were tallied, team “Hey Siri” won the evening and the mustache medallions with a score of 31 out of a possible 43 points. A hearty congratulations to [Alek Åström](https://twitter.com/MisterAlek), [Cezary Wojcik](https://twitter.com/cezary_wojcik), [Kyle Sherman](https://twitter.com/drumnkyle), [Marcus Brissman](https://twitter.com/mbrissman), [Marius Rackwitz](https://twitter.com/mrackwitz), [Melissa Huang](https://twitter.com/meowlissa10), [Nevyn Bengtsson](https://twitter.com/nevyn), and [Rob Stevenson](https://twitter.com/zerogeek)!

Now it’s time for you to play along with the home edition—sharpen your pencil and give it your best!

- Four rounds of ten questions
- Record your answers on a separate sheet of paper
- Each correct answer earns 1 point (unless otherwise specified)
- Play with friends for maximum enjoyment
- Don’t be lame and look things up on the internet or in Xcode

---

## Round 1: General Knowledge

1. In the WWDC keynote, Apple introduced the new ~~OS X~~, er… macOS Sierra. The actual Sierra mountain range is home to the highest peak in the contiguous US. What is the name of that mountain?
2. The Sierra were one focal point of a mass migration to California. What San Francisco sports team has ties to the Sierra during that period in history?
3. Another highlight of the keynote was when Bozoma Saint John introduced the new Apple Music and got the crowd singing along to “Rapper’s Delight”—who recorded the song, and in what year? (2 points)
4. Which version of iPhoto first introduced “Faces and Places?”
5. As part of Foundation’s Swiftification, many classes have lost their `NS` prefixes. Which of these classes remains unchanged so far: `NSBundle`, `NSCalendar`, `NSExpression`, or `NSOperation`?
6. More than just class names have changed—write the new Swift signature for this `NSString` method:

  ```
  func stringByReplacingCharactersInRange(
          _ range: NSRange,
          withString replacement: String) -> String
  ```
7. Write the Swift 3 code to execute an asynchronous “Hello, world!” using GCD.
8. Swift went open source in November and the pace of community contributions has been amazing to see. Within 100, how many pull requests (open, closed, or merged) has the Swift project received on GitHub?
9. Swift was released to the public just over two years ago, but was clearly under development long before that at Apple. What were the month and year of the first commit to the Swift repository?
10. After Chris Lattner, who was the second contributor to Swift? When was their first commit?

## Round 2: Name That Framework

Foundation classes are losing their `NS` prefixes left and right. What would it look like if we got rid of prefixes in every framework? For each question in this round, you’ll be given three classes with their identifying prefix removed. Name the framework that contains all three.

1. Statistic, Sample, Correlation
2. CallObserver, Transaction, Provider
3. Visit, Heading, Region
4. Conversation, Session, Sticker
5. IndexSet, ValueTransformer, Scanner
6. Participant, Reminder, StructuredLocation
7. Circle, LocalSearch, GeodesicPolyline
8. LabeledValue, PhoneNumber, SocialProfile
9. Quadtree, NoiseSource, MonteCarloStrategist
10. RideStatus, PaymentMethod, CarAirCirculationModeResolutionResult

## Round 3: Who _Is_ That?

Many Apple advertisements over the years have featured celebrity voiceovers intoning words of wisdom, inspiration, or at times something else entirely. So pop in your earbuds and for each of the ads below, name the person(s) providing their voice talents.

## Round 4: Easy as 1, 2, 3

Swift is an easy language to learn and use, but its breakneck speed of development has meant breaking changes with each release. For the following snippets of code, answer with the version of Swift that will compile and give the desired result. Because some snippets can run in more than one version, some questions may be worth up to 2 points. Only the major versions are required—for example, if a snippet will run in Swift 2.2, “Swift 2” is a scoring answer.

### 1

```
let a = ["1", "2", "3", "four", "5"]
let numbers = map(a) { $0.toInt() }
let onlyNumbers = filter(numbers) { $0 != nil }
let sum = reduce(onlyNumbers, 0) { $0 + $1! }
// sum == 11
```

### 2

```
let a = ["1", "2", "3", "four", "5"]
let sum = a.flatMap { Int($0) }
           .reduce(0, combine: +)
// sum == 11
```

### 3

```
var a = [8, 6, 7, 5, 3, 0, 9]
a.sort()
print(a)
// [0, 3, 5, 6, 7, 8, 9]
```

### 4

```
var a = [8, 6, 7, 5, 3, 0, 9]
sort(a)
print(a)
// [0, 3, 5, 6, 7, 8, 9]
```

### 5

```
var a = [8, 6, 7, 5, 3, 0, 9]
a.sort()
print(a)
// [8, 6, 7, 5, 3, 0, 9]
```

### 6

```
for i in stride(from: 3, to: 10, by: 3) {
    print(i)
}
// 3
// 6
// 9
```

### 7

```
for i in 3.stride(to: 10, by: 3) {
    print(i)
}
// 3
// 6
// 9
```

### 8

```
enum MyError: ErrorProtocol {
    case Overflow
    case NegativeInput
}

func square(_ value: inout Int) throws {
    guard value >= 0 else { throw MyError.NegativeInput }
    let (result, overflow) = Int.multiplyWithOverflow(value, value)
    guard !overflow else { throw MyError.Overflow }
    value = result
}

var number = 11
try! square(&number)
// number == 121
```

### 9

```
enum MyError: ErrorType {
    case Overflow
    case NegativeInput
}

func squareInPlace(inout value: Int) throws {
    guard value >= 0 else { throw MyError.NegativeInput }
    let (result, overflow) = Int.multiplyWithOverflow(value, value)
    guard !overflow else { throw MyError.Overflow }
    value = result
}

var number = 11
try! squareInPlace(&number)
// number == 121
```

### 10

```
var a: Int[] = [1, 2, 3, 4, 5]
let b = a
a[0] = 100
// b == [100, 2, 3, 4, 5]
```

That’s all! When you’re finished, scroll down a bit for the answers.

.   
   
 .   
   
 .

---

# Answers

## Round 1: General Knowledge

1. Mount Whitney
2. San Francisco 49ers
3. The Sugarhill Gang, 1979 (2 points for both)
4. iPhoto ’09
5. `NSExpression`
6. One of:

  ```
  // 1
  replacingCharacters(in: NSRange, with: String)

  // 2
  func replacingCharacters(
          in range: NSRange,
          with replacement: String) -> String
  ```
7. One of:

  ```
  // 1
  let queue = DispatchQueue(label: "quiz")
  queue.async {
      print("Hello, world!")
  }

  // 2
  DispatchQueue.main.async {
      print("Hello, world!")
  }
  ```
8. 3,012 as of June 14th, 2016 (correct if between 2,912 and 3,112)—[check here](https://github.com/apple/swift/pulls) for the current stats
9. July 2010 (1 point if correct year, 2 if both)
10. Doug Gregor, July 2011 (2 points)

## Round 2: Name That Framework

1. HealthKit
2. CallKit
3. Core Location
4. Messages
5. Foundation
6. EventKit
7. MapKit
8. Contacts
9. GamePlayKit
10. Intents

## Round 3: Who _Is_ That?

1. [Jimmy Fallon & Justin Timberlake](https://www.youtube.com/watch?v=4_dddBsNeSE) (2 points for both)
2. [Martin Scorsese](https://www.youtube.com/watch?v=fGvmZsAuhK4)
3. [Jeff Goldblum](https://www.youtube.com/watch?v=Xvbuwfawqcc)
4. [Lake Bell](https://www.youtube.com/watch?v=oU-_O9gslgo)
5. [Kiefer Sutherland](https://www.youtube.com/watch?v=prImvDVHzTM)
6. [Robin Williams](https://www.youtube.com/watch?v=1mYCIKTX0ug)
7. [Jony Ive](https://www.youtube.com/watch?v=ibklpzKai-o)
8. [Jeff Daniels](https://www.youtube.com/watch?v=a1ml3fyYZaw)
9. [Richard Dreyfuss](https://www.youtube.com/watch?v=tjgtLSHhTPg)
10. [Drunk Jeff Goldblum](https://www.youtube.com/watch?v=dQmK1CnwOUI)

## Round 4: Easy as 1, 2, 3

_If you listed multiple versions, all must be correct for the answer to score._

1. Swift 1
2. Swift 2 or 3 (2 points for both)
3. Swift 3
4. Swift 1
5. Swift 2
6. Swift 1 or 3 (2 points for both)
7. Swift 2
8. Swift 3
9. Swift 2
10. Initial beta release of Swift

---

How’d you do? [Tweet out your score](https://twitter.com/share?text=Woohoo%20@NSHipster%20Pub%20Quiz!%20%F0%9F%A4%93%E2%9C%8D%EF%B8%8F%F0%9F%8D%BB%F0%9F%8E%89) to see how you stack up to your peers!
