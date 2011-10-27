import urllib, HTMLParser, re

class getyoutubecc():
    """ This class allows you to download the caption from a video from you tube
        Example:
            >>> import getyoutubecc
            #import the library
            >>> cc = getyoutubecc.getyoutubecc('2XraaWefBd8','en')
            # Now in cc.caption_obj are the parsed captions, its syntax is like:
            # [{'texlines': [u"caption first line", 'caption second line'],
            #    'time': {'hours':'1', 'min':'2','sec':44,'msec':232} }]
            # Modify the caption as you want if desired
            >>> cc.writeSrtFile('captionsfile.srt')
            #write the contents to a srt file
        TODO:
            - The 
    """
    
    caption_obj = {}

    """ This object contains the fetched captions. Use this to treat the captions or whatever"""
    def __init__(self, video_id, lang="en"):
        """ """
        #Obtain the file from internet
        try:
            cc = urllib.urlopen("http://www.youtube.com/api/timedtext?v=" + video_id + "&lang=" + lang).read() 
        except:
            print "Problem with connection"
        #parse the file to make a easy to modify object with the captions and its time
        self.caption_obj = self._parseXml(cc);

    def writeSrtFile(self,filename="caption"):
        srt_lines = self._generateSrt(self.caption_obj) #generate the srt file
        srtfile = open(filename,'w')
        for line in srt_lines:
            srtfile.write(line+"\n")

    def _parseXml(self,cc):
        """ INPUT: XML file with captions
            OUTPUT: parsed object like:
                [{'texlines': [u"So, I'm going to rewrite this", 'in a more concise form as'],
                'time': {'hours':'1', 'min':'2','sec':44,'msec':232} }]
        """
        htmlpar = HTMLParser.HTMLParser()
        cc = cc.split("</text>") # ['<text start="2997.929">So, it will\nhas time', '<text start="3000.929">blah', ..]
        captions = []
        for line in cc:
            if re.search('text', line):
                time = re.search(r'start="(\d+)(?:\.(\d+)){0,1}', line).groups() # ('2997','929')
                time = ( int(time[0]), int(0 if not time[1] else time[1]) )
                    #convert seconds and millisec to int
                text = re.search(r'">(.*)', line, re.DOTALL).group(1) # extract text i.e. 'So, it will\nhas time'
                textlines = [ htmlpar.unescape(htmlpar.unescape(lineunparsed)) for lineunparsed in text.split('\n') ] 
                    #unscape chars like &amp; or &#39;
                ntime = {'hours':time[0]/3600,"min":time[0]%3600/60,"sec":time[0]%3600%60,"msec":time[1]}
                captions.append({'time':ntime,'textlines':textlines})
        return captions

    def _generateSrt(self,captions):
        """ INPUT: array with captions, i.e.
                [{'texlines': [u"So, I'm going to rewrite this", 'in a more concise form as'],
                'time': {'hours':'1', 'min':'2','sec':44,'msec':232} }]
            OUTPUT: srtformated string
        """
        caption_number = 0
        srt_output = []
        for caption in captions:
            caption_number += 1
            #CAPTION NUMBER
            srt_output.append(str(caption_number))
            #TIME
            time_from = ( caption['time']['hours'], caption['time']['min'], caption['time']['sec'], caption['time']['msec'] ) 
            if len(captions)>caption_number:
                #display caption until next one
                next_caption_time = captions[caption_number]['time']
                time_to = ( next_caption_time['hours'], next_caption_time['min'], next_caption_time['sec'], next_caption_time['msec'] )
            else:
                #display caption for 2 seconds
                time_to = (time_from[0],time_from[1]+2,time_from[2],time_from[3]) 
            srt_output.append( (":").join([str(i) for i in time_from[0:-1]])+","+str(time_from[-1])+" --> "+(":").join([str(i) for i in time_to[0:-1]])+","+str(time_to[-1]))
            #CAPTIONS
            for caption_line in caption['textlines']:
                srt_output.append(caption_line)
            #Add two empty lines to serarate every caption showed
            srt_output.append("")
            srt_output.append("")
        return srt_output

        
if __name__ == "__main__":
    import sys
    sys.argv
    for vid in sys.argv[1:]:
        print "downloading " + vid + " captions"
        cc = getyoutubecc(vid)
        cc.writeSrtFile(vid+'.srt')
