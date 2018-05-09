---
layout: post
title:  "THE JOURNEY"
date:   2018-04-12 00:00:00 +0000
categories: all life
---

We had a great trip

This is code we did develop:

{% highlight python %}
# Basic I/O with HID
class _HID:
    @staticmethod
    # Write the data buffer to the HID given by hidraw_number
    def write(hidraw_number, data):
        dev = os.open("/dev/hidraw" + str(hidraw_number), os.O_WRONLY)
        ret = os.write(dev, data)
        os.close(dev)
        return ret

    @staticmethod
    # Read the hex dump of the HID given by hidraw_number and return it as a string
    def read(hidraw_number):
        dev = os.open("/dev/hidraw" + str(hidraw_number), os.O_RDONLY)
        data = os.read(dev, 6)
        os.close(dev)
        return data.encode("hex")
{% endhighlight %}

__Higlight__
_Italyc_
