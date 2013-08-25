DESCRIPTION
=======================================================

This class allows you to download the caption from a video from you tube


PYTHON CLASS USAGE
-------------------------------------------------------

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
         
         Notes:
           MULTITRACK VIDEO
           if video is a multitrack video (or the track has a name) you need
           to specify the name of the track:
            >>> cc = getyoutubecc.getyoutubecc('pNiFoYt69-w','fr','french')
           TRANSLATE VIDEO
           if you prefer the automatic translation to another language use 
           the lang code
            >>> cc = getyoutubecc.getyoutubecc('pNiFoYt69-w','fr','french', tlang:'es')


COMMAND LINE USAGE
-------------------------------------------------------

If you prefer the command line version of this, or just to test it:

            $ ./getyoutubecc.py -h
            getyoutubecc -v <video_id> -l <language_id> [-t <track_name>] [-T <translate_to>]
            Example: getyoutubecc -v pNiFoYt69-w -l fr -t french -T es
            Example: getyoutubecc -v 2XraaWefBd8 -l en 
            NOTE: if video has a track name, the -t argument is mandatory 

COPYRIGHT
-------------------------------------------------------

this code is released into the public domain by the copyright holders.

TODO
-------------------------------------------------------

- Test the code, different languages in diferent videos for instance
- Improve regular expresion
- Add support for the automatic generate captions service in youtube
