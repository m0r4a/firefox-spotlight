# First draft 

I started this project by doing a kinda simple code, just read the .json that I've created and open firefox using that json as repalacement for the bookmarks of firfox.

# Second draft

Now I'm trying to de-compress the original bookmarks file since its a .jsonlz4 file. I'm using the lz4 library to do that.

So next step is to create a separate folder and experiment with the lz4 library to see if I can decompress the file and how does the json looks like.

Looks like I successfully decompressed the file, maybe using the user's bookmarks file can be an optinal feature?

_Note: I really don't mind that everyone can see my bookmarks, so I can publish the code with my bookmarks file as an example without any problem._
