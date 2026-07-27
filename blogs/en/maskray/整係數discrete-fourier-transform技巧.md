---
title: 整係數Discrete Fourier transform技巧
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2016-10-03-discrete-fourier-transform'
original_language: en
published: 2016-10-03
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fd5c36c6f9a4d7ce'
translated: false
---

> 原文：[整係數Discrete Fourier transform技巧](https://maskray.me/blog/2016-10-03-discrete-fourier-transform)　·　MaskRay (宋方睿)

[2016-10-03](https://maskray.me/blog/2016-10-03-discrete-fourier-transform)

# 整係數Discrete Fourier transform技巧

## Discrete Fourier transform

向量的DFT 定義爲：

其中是primitive root of unity of order ，即：且。 通常取或。

## Inverse transform

性質： (j模n爲0時取1，否則取0)

因此

假設加減乘除時間複雜度爲，樸素實現的時間複雜度爲。 Cooley–Tukey algorithm是最常見的fast Fourier transform算法，時間複雜度爲。 有radix-2、radix-4、split-radix等多種形式。

注意使用的是DFT用的係數的倒數。如果使用DFT實現IDFT可以先翻轉向量： 1  
2  
3  
4  
5  
6  
reverse(a+1, a+n);  
  
// compute DFT  
  
for (long i = 0; i \< n; i++)  
 a[i] *= 1.0/n;

## Decimation in time FFT

Cooley-Tukey是一種radix-2分治算法，把偶數下標的子序列的Fourier transform與奇數下標的子序列的Fourier transform，用時間合併。

Decimation in time在變換之後對下標進行bitreverse操作。

使用Stockham FFT可以省去bitreverse操作。

## Decimation in frequency FFT

Sande-Tukey是另一種radix-2分治算法，把前一半子序列的Fourier transform與後一半子序列的Fourier transform，用時間合併。

Decimation in frequency在變換之前對下標進行bitreverse操作。如果Decimation in time的DFT與Decimation in frequency的IDFT一起用，可以省略兩處bitreverse操作。

DIF的bufferfly操作不適合fused multiply-add。

## Memory-bound

FFT是memory-bound的。比較快的實現會在N較大時使用遞歸，而N較小時使用迭代。

## Number theoretic transform

DFT可以用於複數以外的其他ring，常用於。

使用128 bits模數需要高效的`u64*u64%u64`，其中模數是常數。

### 硬件除法指令(32 bits、64 bits)

`DIV`指令性能很低。

```c
extern inline u64 mul_mod(u64 a, u64 b, u64 m)
{
  u64 r;
  asm("mulq %2\n\tdivq %3" : "=&d"(r), "+a"(a) : "rm"(b), "rm"(m) : "cc");
  return r;
}
```

到AVX-512也沒有提供把兩個64 bits乘數的積放在一個128 bits寄存器的指令，GCC沒有提供用乘法、移位等模擬的u128除以u64的常量除法。

### 64位mantissa浮點數(32 bits、64 bits)

當模數時可以用64位mantissa浮點數計算`u64*u64%u64`。

由等式

兩邊模，得

即用`u64`乘法計算的低64位，減去的低64位。其中，可以用64位mantissa浮點數(Intel x87 80-bit double-extended precision)計算，再round成`u64`。

round時若向上取整了，減數會大於被減數。若，可以根據差的符號位判斷。

```c
u64 mul_mod(u64 a, u64 b, u64 P)
{
  u64 x = a*b, r = x - P*u64((long double)a*b/P+0.5);
  return i64(r) < 0 ? r + P : r;
}
```

存儲的倒數，用`(long double)a*b*Q`代替`(long double)a*b/P`能快些。此時會引入額外的誤差，Matters Computational說適用於，原因不明。

### 編譯器生成的常量除法(32 bits)

對於固定的模，GCC/llvm可以生成`u64%u32`的高效代碼。llvm的`lib/Transforms/Utils/IntegerDivision.cpp`。

### Montgomery modular multiplication+Barret reduction(32 bits)

Faster arithmetic for number-theoretic transforms，用乘法和移位代替除法。

快速計算`u64%u32`，用乘法和移位代替除法。設，爲大於等於的整數，爲負整數。

，是的估計值，若大於等於則減去的倍數。

因此

令，則，即估計值最多小2，最多兩個conditional move指令(`if (r >= P) r -= P;`)即可修正餘數。

令，則估計值最多小1。

```c
extern inline u64 barrett_30_2(u64 a, u64 P, u64 M)
{ // 2^29 < P < 2^30, M = floor(2^61/P)
  u64 r = a-((a>>28)*M>>33)*P;
  if (r >= P) r -= P;
  return r;
}

extern inline u64 barrett_30_1(u64 a, u64 P, u64 M)
{ // 2^29 < P < 2^30, M = floor(2^60/P)
  u64 r = a-((a>>29)*M>>31)*P;
  if (r >= P) r -= P;
  if (r >= P) r -= P;
  return r;
}
```

當模數爲常量時，該算法不如編譯器生成的常量除法。若模數不固定時可以考慮使用。

## Cyclic convolution

兩個長爲的序列與的cyclic convolution的長度也是。第項定義爲：

## Linear convolution

兩個長爲的序列與的linear convolution的長度是。

第項總是0。多項式乘法是一種常見的linear convolution應用。

Zero pad原序列到長度後，計算cyclic convolution即可得到linear convolution。

## 範圍和精度

向量卷積需要注意精度問題。

使用`complex<double>`計算convolution，需要保證結果每一項的實數部分在(`Number.MIN_SAFE_VALUE`、`Number.MAX_SAFE_INTEGER`)範圍內，是double能精確表示的最大整數。採取round half to even規則，均表示爲，無法區分。

設每項係數的絕對值小於等於，那麼convolution結果每一項絕對值小於等於，若則可放心使用`complex<double>`。

`complex<double>`還要受到浮點運算誤差影響。根據Roundoff Error Analysis of the Fast Fourier Transform，沒仔細看，relative error均值爲`log2(n)*浮點運算精度*變換前係數最大值`，對於結果，這個量達到就很可能出錯。增長速度可以看作是，不如。因此通常不必擔心浮點運算的誤差。

對於模的number theoretic transform，，若則可放心使用。

關於精度，另外可參考[https://github.com/simonlindholm/fft-precision/blob/master/fft-precision.md](https://github.com/simonlindholm/fft-precision/blob/master/fft-precision.md)。

1004535809 (=479*2**21+1), 998244353 (=119*2**23+1), 897581057 (=107*2**23+1)，這三個數均小於，兩倍不超過`INT32_MAX`(兩個+-P之間的數加減不會超出int32_t表示範圍)，且可表示爲，其中爲2的冪，適合用作number theoretic transform的模。3是它們共同的原根。 另一个候選素數爲880803841 (=105*2**23+1)，26是一個原根。

設係數取自的uniform distribution，則係數均值爲，方差爲。若把係數平移至，則係數均值，方差爲。若其中之一independent and identically distributed，則方差會很小。可以用Chebyshev's inequality等估計係數絕對值，上界可以減小。即使不是independent and identically distributed，也可以用來計算，是independent and identically distributed uniform 。

下面考察模P多項式乘法，碰到精度問題時的兩種應對方案：sqrt decomposition、Chinese remainder theorem。

## 方案0：sqrt decomposition(FFT, NTT)

適用於FFT與NTT。 取爲接近的整數，分解、，則：

適當選擇可以使的係數小於等於，convolution結果係數最大值爲，比原來的小。

求出後，計算等式右邊四個convolution，帶權相加即得到原convolution。

如上樸素方案需要4次長爲的DFT、1次長爲的inverse DFT。

一種優化方案是使用Toom-2 (Karatsuba)計算，可以減少爲3次DFT、1次inverse DFT。。

容易擴展到cube root decomposition等。對於number theoretic transform，分成份需要個DFT和個IDFT，不如用Chinese remainder theorem。

### 優化0：實部表示低位、虛部表示高位

FFT可以計算複數的DFT，但在樸素的多項式乘法中，FFT只作用於實數向量，虛數部分浪費了。 sqrt decomposition把一個係數拆分成兩項，我們可以把兩項裝載到實數部分和虛數部分。 具體方法如下：

取正整數與接近且是一個儘可能小的正整數。

分解、。 考察如下的變換：

注意每一項絕對值的值域變爲倍了，因此計算對精度有更高的要求。取較小的可以降低精度要求。

右邊同餘於。 提取虛部與實部，將虛部除以再乘以，再加上實部即得：

正是我們需要的形式。

這個優化需要2次長爲的DFT、1次長爲的inverse DFT。

### 優化1：正交計算兩個實係數向量DFT(FFT)

這是另一種利用向量的虛數部分的方法。

的共軛的DFT可由的DFT求出：

換言之，計算一個複數向量的DFT，可以通過簡單變換，得到實數部分向量的DFT與實數部分向量的DFT。買一送一。

分解、後，根據上面的公式，用計算和，同法計算和。然後用計算出與，同法計算出與。

需要2次長爲的DFT、2次長爲的inverse DFT。

### 奇偶項優化(FFT)

該優化可以和其他方式疊加。

把看作多項式，同樣地，看作多項式。

偶次項, 奇次項，同樣地，定義與。的係數爲，的係數爲，令其長爲，高位用填充。

用正交計算兩個實係數向量DFT的方式，用2次長度爲(之前都是 )的DFT計算, 。循環右移1位的DFT的第項等於，因此根據的DFT的係數可以得到的DFT的係數。

構造長爲的向量：

的實部爲結果的偶次項係數，虛部爲結果的奇次項係數。

需要2次長爲的DFT、1次長爲的inverse DFT。

## 方案1：Chinese remainder theorem(NTT)

適用於NTT。 取個可用於number theoretic transform的質數，使，計算個NTT，之後用Chinese remainder theorem合併。

求有至少兩種算法。

### 經典算法(Gauss's algorithm)

Gauss之前也有很多人提出。

對於每個用Blankinship's algorithm計算。

注意可能超出機器single-precision表示範圍，該算法不適合求。

### Garner's algorithm

定義

滿足前個方程，滿足所有方程。

稍加變形可用於求。

原來的每個是精確值，現在只有的結果，因此計算時之前的都不可復用，需要重新計算。時間複雜度上升爲。

## 測試

[https://gist.github.com/MaskRay/fac2042058dd5d9e59953f18f3f3978a](https://gist.github.com/MaskRay/fac2042058dd5d9e59953f18f3f3978a)

NTT int使用小于的素数，编译器用乘法模拟常数除法。 NTT long，编译器无法优化常数除法，性能很低，使用浮点mul_mod会略快于128位除以64位的DIV指令。

```plaintext
n	microseconds	algorithm

131072  3860    NTT dit2 int
131072  6104    FFT dif2
131072  6712    FFT dit2
131072  6912    NTT dif2 int
131072  6936    Montgomery+Barrett NTT dif2 int
131072  9592    NTT dif2 long non-constant P
131072  10122   NTT dit2 long
131072  13169   NTT dif2 int non-constant P
131072  15419   NTT dif2 long

262144  8993    NTT dif2 int
262144  9036    NTT dit2 int
262144  9670    Montgomery+Barrett NTT dif2 int
262144  15484   FFT dit2
262144  17601   FFT dif2
262144  19731   NTT dit2 long
262144  20527   NTT dif2 long non-constant P
262144  21910   NTT dif2 long
262144  29457   NTT dif2 int non-constant P

524288  18502   NTT dif2 int
524288  20110   Montgomery+Barrett NTT dif2 int
524288  23156   NTT dit2 int
524288  39890   FFT dif2
524288  39904   FFT dit2
524288  44145   NTT dif2 long non-constant P
524288  45038   NTT dit2 long
524288  46334   NTT dif2 long
524288  65265   NTT dif2 int non-constant P

1048576 43648   NTT dit2 int
1048576 45704   NTT dif2 int
1048576 46167   Montgomery+Barrett NTT dif2 int
1048576 104362  NTT dit2 long
1048576 107571  NTT dif2 long non-constant P
1048576 119743  FFT dif2
1048576 122029  NTT dif2 long
1048576 122174  FFT dit2
1048576 144370  NTT dif2 int non-constant P

2097152 122989  Montgomery+Barrett NTT dif2 int
2097152 137276  NTT dif2 int
2097152 143955  NTT dit2 int
2097152 293222  FFT dif2
2097152 338580  FFT dit2
2097152 352833  NTT dif2 int non-constant P
2097152 360372  NTT dif2 long non-constant P
2097152 422108  NTT dit2 long
2097152 423817  NTT dif2 long

4194304 455859  NTT dit2 int
4194304 467340  NTT dif2 int
4194304 490114  Montgomery+Barrett NTT dif2 int
4194304 779945  FFT dif2
4194304 839698  FFT dit2
4194304 904096  NTT dit2 long
4194304 956174  NTT dif2 long
4194304 969572  NTT dif2 long non-constant P
4194304 1074858 NTT dif2 int non-constant P

8388608 1052072 NTT dit2 int
8388608 1138089 NTT dif2 int
8388608 1189775 Montgomery+Barrett NTT dif2 int
8388608 1737166 FFT dif2
8388608 1839095 FFT dit2
8388608 2053195 NTT dif2 long
8388608 2072172 NTT dif2 long non-constant P
8388608 2186451 NTT dit2 long
8388608 2893584 NTT dif2 int non-constant P
```

花哨的Montgomery+Barrett不如常量除法的NTT int，好處是一份代碼可以適用於多個模數，而NTT int得用template或其他方式爲各個模數生成不同代碼。

不受到Level 3 cache制約時，Montgomery NTT只需要NTT int 60%的時間，此時每次重新計算unit root代替lookup table會快些。

一般來說，decimation in frequency(Sande-Tukey，從較大的n計算到較小的n)優於decimation in time(Cooley-Tukey，從較小的n計算到較大的n)，可能是因爲decimation in frequency的butterfly數據依賴小些。

FFT有超過10%時間花在計算unit roots上，而NTT只有5%。考慮到FFT往往能正交計算兩個序列，而NTT只能計算一個，且double有53位精度而NTT int只能使用以下的素數(當前代碼只能處理以下的)，FFT通常優於NTT。

## References

感謝ftiasch老師教導。

- 黄嘉泰(fotile96), [https://async.icpc-camp.org/d/408-fft](https://async.icpc-camp.org/d/408-fft)
- Jörg Arndt, Matters Computational
- Handbook of Applied Cryptography
- 毛嘯，再探快速傅裏葉變換，2016年信息學奧林匹克中國國家隊候選隊員論文集
- [Faster arithmetic for number-theoretic transforms](https://arxiv.org/pdf/1205.2926.pdf)
- [Speeding Up Barrett and Montgomery Modular Multiplications](http://homes.esat.kuleuven.be/~fvercaut/papers/bar_mont.pdf)

uwi，[https://www.hackerrank.com/rest/contests/w23/challenges/sasha-and-swaps-ii/hackers/uwi/download_solution](https://www.hackerrank.com/rest/contests/w23/challenges/sasha-and-swaps-ii/hackers/uwi/download_solution)：Modified Montgomery+Barrett變體+Garner's algorithm：
