---
title: SoundMeter
apple_id: DTS10000997
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SoundMeter/Listings/src_StatusPrinter_java.html
archived_at: '2026-07-18T03:25:05.107470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SoundMeter](SoundMeter.md)


[Next](Document%20Revision%20History.md)[Previous](src-SoundMeter.java.md)

# src/StatusPrinter.java

```
import quicktime.*;
import quicktime.app.time.*;
import quicktime.std.clocks.*;
import quicktime.std.movies.media.*;

class StatusPrinter implements Ticklish {

    private AudioMediaHandler mh;
    private int numBands;
    private int[] freqs;
    StatusPrinter(AudioMediaHandler mh, int num, int[] freqs) {
        this.mh = mh;
        numBands = num;
        this.freqs = freqs;
    }

    public boolean tickle (float er, int time) throws QTException {
        getInfo();
    //  System.out.println ("tickle:er=" + er + ",time=" + time);
        return true;
    }

    public void timeChanged (int time) throws QTException {
    //  new Exception().printStackTrace();
    //  System.out.println ("tc:" + time);
        for (int i = 0; i < numBands; i++) {
            int f = freqs[i];
            String str = null;
            if (f >= 1000) {
                if (f % 1000 != 0)
                    str = Integer.toString (f / 1000) + ".5\t";
                else
                    str = Integer.toString (f / 1000) + "\t";
            } else
                str = Integer.toString (f) + "\t";
            System.out.print (str);
        }
        System.out.println ("\n___________________________________________________________________________________________");
    }

    public void getInfo() throws QTException {
        int[] levels = mh.getSoundEqualizerBandLevels (numBands);
        for (int i = 0; i < numBands; i++)
            System.out.print (levels[i] + "\t");
        System.out.println ("");
    //  System.out.println (mh.getSoundEqualizerBands(8));
    }

}
```

[Next](Document%20Revision%20History.md)[Previous](src-SoundMeter.java.md)

