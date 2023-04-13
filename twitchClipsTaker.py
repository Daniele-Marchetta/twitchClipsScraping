from data import data_obj,filters
from functions import get_clips


headers = {"Client-ID":"kimne78kx3ncx6brgo4mv6wki5h1ko"}

#array di Twitchclips
clips = get_clips("valorant",3,[],filters.LAST_DAY.name)
#filtered_clips=filter_by_tags(clips,['insane'])
#for clip in clips:
   # for parola in filtroParole:
    #    if (parola in clip['node']['title'].lower()):
     #       filteredClips.append(TwitchClips(clip['node']['title'],clip['node']['broadcaster'],clip['node']['url'],clip['node']['durationSeconds'],str(clip['node']['thumbnailURL']),clip['node']['createdAt'],clip['node']['game']['boxArtURL']))
            
#tags = getTikTokTags("valorant")
#print(len(filteredClips))
#for singleclip in filteredClips:
 #   print(singleclip.url)
  #  print(singleclip.data_creazione)
for p in clips:
    print(p.url)



