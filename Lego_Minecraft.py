#variables and initializing

if __name__ == '__main__':
    from init import *
#for x in golemwolf.keys():
     #print(x)
#for x in wolfking.keys():
    #print(x)
#print(golemwolf, wolfking)
#main loop

#pracvtice online ypthon

#########################
#create wpm test
#########################


while True:

    #screen and backround
    screen.fill((0,0,0))

    screen.blit(backround,(0,0))
    
    #display character information
    if characters and main_menu != True:
        test = id(characterchoice, kinggolem[characterchoice][0], kinggolem[characterchoice][1], kinggolem[characterchoice][2])
        test.create_id()

    else:
        characters = False
#add repeat button
  
    #music
    if other_music == False:
        if pygame.mixer.music.get_busy() == 0:
            #musicchoice = random.choice(['Sounds/haggstorm.mp3', 'Sounds/mice_on_venus.mp3', 'Sounds/minecraft.mp3', 'Sounds/wet_hands.mp3', 'Sounds/sweden.mp3'])
            if queue != '':
                playqueue(queue, False)
                music_message_timer = 0

            elif shuffle:
                shuffle_music = shuffle_play(music_list)
                music_message_timer = 0
                
            elif shuffle_playlist:
                shuffle_playlist_music = shuffle_play(playlist[playlist_keys[playlist_choice]])
                print(shuffle_playlist_music)
                music_message_timer = 0
            else:
                queue = playqueue(queue, True)
                pygame.mixer.music.load(musicchoice)
                music_playing = musicchoice
                seconds = 0
                pygame.mixer.music.play()
                music_message_timer = 0
        
        elif music_message_timer < 1:
            #make function with condition detection
            if queue != '':
                music_choice_display = queue
                music_text_2 = golem(music_choice_display, cyan, (width/2+150,height-50), font)
                music_text_1.KING()
                music_text_2.KING()
                music_message_timer += 0.01
            elif shuffle:
                music_choice_display = shuffle_music
                music_text_2 = golem(music_choice_display, cyan, (width/2+150,height-50), font)
                music_text_1.KING()
                music_text_2.KING()
                music_message_timer += 0.01
            elif shuffle_playlist:
                music_choice_display = shuffle_playlist_music
                music_text_2 = golem(music_choice_display, cyan, (width/2+150, height-50), font)
                music_text_1.KING()
                music_text_2.KING()
                music_message_timer += 0.01
            else:
                music_choice_display = music_display(musicchoice)
                music_text_2 = golem(music_choice_display, cyan, (width/2+150,height-50), font)
                music_text_1.KING()
                music_text_2.KING()
                music_message_timer += 0.01
        elif queue != '':
            queue = playqueue(queue, True)
    else:
        if pygame.mixer.music.get_busy() == 0 and repeat == False:
            other_music = False
    
    
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            os.remove(os.getcwd() + '\\Playlists.txt')
            time.sleep(1)
            playlist_create_new = open('Playlists.txt', 'w')
            playlist_create_new.write(str(playlist))
            playlist_create_new.close()
            sys.exit()
     

        if event.type == pygame.KEYDOWN:
            if event.key == K_e:
                os.remove(os.getcwd() + '\\Playlists.txt')
                time.sleep(1)
                playlist_create_new = open('Playlists.txt', 'w')
                playlist_create_new.write(str(playlist))
                playlist_create_new.close()
                pygame.quit()

            
            if playlist_create == True:
                
                if event.key == K_RETURN:
                    if playlist_new_name in playlist or len(playlist_new_name.replace(' ', '')) == 0 or len(playlist_new_name) >=18:
                        
                        playlist_create_new_error = True
                    else:

                        playlist[playlist_new_name] = []
                        playlist_keys.append(playlist_new_name)
                        playlist_manage_box_display = buttontextbox(screen, pygame.Rect(100, 250, 400, 600), playlist_keys, [400,100], font, 102)
                        playlist_new_name = ''
                        playlist_create = False
                        if len(playlist_keys) != 0:
                            playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)
                            playlist_name = button(str(playlist_keys[playlist_choice]), (width-500, 150), (0,0,102), font, (400,70), cyan)
                            playlist_duration = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/3600))+":"+"0"*(2-len(str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))))+str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)
                            playlist_manage_title = golem('Manage Playlists', cyan, (300,200), font)
                        else:
                            playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), [], [400,100], font, 102)
                            playlist_name = button('You Have No Playlists', (width-500, 150), (0,0,102), font, (400,70), cyan)
                            playlist_duration = button('', (width-150, 220), (0,0,102), font, (400,30), cyan)
                            playlist_manage_title = golem('Create a New Playlist to Manage', cyan, (300,200), font)
                            
                elif event.key == K_BACKSPACE:
                   
                    playlist_new_name = playlist_new_name[:-1]
           
                else:
                    playlist_new_name += event.unicode
            if event.key == K_w: 
                pygame.mixer.music.stop()
            if event.key == K_f:
                if fullscreen == True:
                    
                    screen = pygame.display.set_mode(size)
                    width = screen.get_width()
                    height = screen.get_height()
                    fullscreen = False
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                else:

                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    width = screen.get_width()
                    height = screen.get_height()
                    fullscreen = True
                    music_text_1 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                    
            if event.key == K_p:
                patchnotes = open('updates.txt', 'r')
                patchnotesread = patchnotes.read()
                patchnotes.close()
                print(patchnotesread)
            if event.key == K_UP:
                volumeup = True
                
            if event.key == K_DOWN:
                volumedown = True

            if event.key == K_b:
                main_menu = True
            
            if event.key == K_k:
                if music_pause == False:
                    pygame.mixer.music.pause()
                    music_pause = True            
                else:
                    pygame.mixer.music.unpause()
                    music_pause = False
                
            if event.key == K_q and music == True:
                try:          
                    if index1 != -69:
                        queue = music_list[index1]
                        queue_timer = 0
                except NameError:
                    pass
              
             
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                volumeup = False

            if event.key == K_DOWN:
                volumedown = False
    
        if event.type==pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                if music:
                    index2=playlist_box_display.clickbuttons(pygame.mouse.get_pos())         
                    if len(playlist_keys) != 0:
                        indexfunction(index2, playlist_box_display, playlist[playlist_keys[playlist_choice]])

                
                     
                      

                    if pygame.mouse.get_pos()[0] > width-1010 and pygame.mouse.get_pos()[0] < width-940 and pygame.mouse.get_pos()[1] > height-80 and pygame.mouse.get_pos()[1] < height:
                        print('golem')
                        pygame.mixer.music.load(random.choice(["Sounds/Music/TOP_SECRET/playplaykinggolemwolf.mp3", "Sounds/Music/TOP_SECRET/kingkingking.mp3", "Sounds/Music/TOP_SECRET/LGBTIIIIIIIIIIIIIIIIIIIII.mp3"])) #yes here it finally is
                        pygame.mixer.music.play()




                    elif music_box.clickbuttons(pygame.mouse.get_pos()) == -69 and playlist_box_display.clickbuttons(pygame.mouse.get_pos()) == -69:
                        pass
                    
                    elif playlist_box_display.clickbuttons(pygame.mouse.get_pos()) >= 0:
                        other_music = True
                        music_text_3 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                        music_text_4 = golem(playlist[playlist_keys[playlist_choice]][playlist_box_display.clickbuttons(pygame.mouse.get_pos())], cyan, (width/2+150,height-50), font)    
                        other_music_load = 'Sounds\\Music\\' +  playlist[playlist_keys[playlist_choice]][playlist_box_display.clickbuttons(pygame.mouse.get_pos())] + '.mp3'
                        music_playing = other_music_load
                        seconds = 0
                        pygame.mixer.music.load(other_music_load)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.play()
                        music_message_timer = 0
                    

                    


                    else:
                        other_music = True
                        index1=music_box.clickbuttons(pygame.mouse.get_pos())
                        indexfunction(index1, music_box, music_list, indexlist=returnindices(bass_boosted_music, music_list), color=purpleblue, list_color=(255,255,0))
                        music_text_3 = golem('NOW PLAYING:', cyan, (width/2-150, height-50), font)
                        music_text_4 = golem(music_list[music_box.clickbuttons(pygame.mouse.get_pos())], cyan, (width/2+150,height-50), font)    
                        other_music_load = 'Sounds\\Music\\' + music_list[music_box.clickbuttons(pygame.mouse.get_pos())] + '.mp3'
                        music_playing = other_music_load
                        seconds = 0
                        pygame.mixer.music.load(other_music_load)
                        pygame.mixer.music.stop()
                        pygame.mixer.music.play()
                        music_message_timer = 0
                #put into function
                
                elif manage_playlist:
                    index3=playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos())
                    indexfunction(index3, playlist_manage_box_display, playlist_keys)
                    #index4=playlist_manage_box_display_options.clickbuttons(pygame.mouse.get_pos())  
                    #change color when clicked to stand out more
                    #indexfunction(index4, playlist_manage_box_display_options, music_list)
                    '''
                    index = playlist_manage_box_display_options.clickbuttons(pygame.mouse.get_pos())
                    for x in range(len(music_list)):
                        if music_list[x] in playlist[playlist_keys[playlist_manage_choice]]:
                            playlist_manage_box_display_options.changebuttoncolor(x, red)
                    '''
                    
                    if playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos()) >= 0:
                        playlist_manage_choice = playlist_keys[playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos())]

                        if playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos()) == playlist_manage_choice:
                            playlist_manage_choice = ''
                        else:
                            playlist_manage_choice = playlist_manage_box_display.clickbuttons(pygame.mouse.get_pos())
                            playlist_manage_box_display_options_title = golem('Add to '+ str(playlist_keys[playlist_manage_choice]), cyan, (width-300, 200), font)
                        
                        indexfunction(0, playlist_manage_box_display_options, music_list, indexlist = returnindices(playlist[playlist_keys[playlist_choice]], music_list)) #make constant
                    if playlist_manage_box_display_options.clickbuttons(pygame.mouse.get_pos()) >= 0:
                        playlist_manage_options = playlist_manage_box_display_options.clickbuttons(pygame.mouse.get_pos())
                        #print(playlist)
                        
                        #print(playlist[playlist_keys[playlist_choice]])
                        #print(playlist[playlist_keys[playlist_manage_choice]])
                        if len(playlist_keys) != 0 :
                            try:
                                if music_list[playlist_manage_options] in playlist[playlist_keys[playlist_manage_choice]]:
                                    pass
                                else:
                                    playlist[playlist_keys[playlist_manage_choice]].append(music_list[playlist_manage_options])

                                    playlist_duration = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/3600))+":"+"0"*(2-len(str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))))+str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)
                                    playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)
                            except TypeError:
                                pass
                    index4=playlist_manage_box_display_options.clickbuttons(pygame.mouse.get_pos()) 
                    indexfunction(index4, playlist_manage_box_display_options, music_list, indexlist = returnindices(playlist[playlist_keys[playlist_choice]], music_list)) #make constant
                      
                        #print(playlist[playlist_manage_choice])
                        #
                        #print(playlist)
                    #print('king')
                music_box.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONDOWN)
                playlist_box_display.clickscroll(pygame.mouse.get_pos(), pygame.MOUSEBUTTONDOWN)
                playlist_manage_box_display.clickscroll(pygame.mouse.get_pos(), pygame.MOUSEBUTTONDOWN)
                playlist_manage_box_display_options.clickscroll(pygame.mouse.get_pos(), pygame.MOUSEBUTTONDOWN)
                startmouseposition=pygame.mouse.get_pos()[1]
                  
                   
                    
                    
            
            elif event.button==4:
                patchnotes_display.scroll("up",pygame.mouse.get_pos())
                music_box.scrollbox("up",pygame.mouse.get_pos())
                playlist_box_display.scrollbox("up", pygame.mouse.get_pos())
                playlist_manage_box_display.scrollbox("up", pygame.mouse.get_pos())
                playlist_manage_box_display_options.scrollbox("up", pygame.mouse.get_pos())
                clubs_display.description.scroll("up", pygame.mouse.get_pos())
  
            elif event.button==5:
                patchnotes_display.scroll("down",pygame.mouse.get_pos())
                music_box.scrollbox("down",pygame.mouse.get_pos())
                playlist_box_display.scrollbox("down", pygame.mouse.get_pos())
                playlist_manage_box_display.scrollbox("down", pygame.mouse.get_pos())
                playlist_manage_box_display_options.scrollbox("down", pygame.mouse.get_pos())
                clubs_display.description.scroll("down", pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                music_box.clickscroll(pygame.mouse.get_pos(),pygame.MOUSEBUTTONUP)
                playlist_box_display.clickscroll(pygame.mouse.get_pos(), pygame.MOUSEBUTTONUP)
                playlist_manage_box_display.clickscroll(pygame.mouse.get_pos(), pygame.MOUSEBUTTONUP)
                playlist_manage_box_display_options.clickscroll(pygame.mouse.get_pos(), pygame.MOUSEBUTTONUP)

    if pygame.mixer.music.get_busy() == 0 and repeat:  
        music_playing = other_music_load
        seconds = 0
        pygame.mixer.music.load(other_music_load)
        pygame.mixer.music.play()
        music_message_timer = 0 
        test_count += 1
    #print(queue)
    
    if queue_timer < 1:
        queue_text_2 = golem(queue, cyan, (width/2+150, height-100), font)
        queue_text_1.KING()
        queue_text_2.KING()
        queue_timer += 0.01
    
 
    #if shuffle:
        #shuffle_text_display.KING()
        
  
    #volume control
    if volumeup and volume <= 0.99:
        volume += 0.01
        pygame.mixer.music.set_volume(volume)
     
    if volumedown and volume >= 0.01:
        volume -= 0.01
        pygame.mixer.music.set_volume(volume)
    if volumeup or volumedown:
        volume_display = golem(str('%.0f' % (volume*100)), cyan, (width-50,height-250), font)
        volume_display.KING()
   

    if other_music:
        if music_message_timer >= 1:
            pass
            
            
        elif music_message_timer < 1:
            music_text_3.KING()
            music_text_4.KING()
            music_message_timer += 0.01
    
        
    
    
    #title
    text = KINGOUTLINE(screen, 'Lego Minecraft Database', (width/2, height-(height-100)), font, red)
    
    #moon and sun
    if night:
        screen.blit(moon, (width-125, height-(height-50)))#sun and moon 200x200

    if day:
        screen.blit(sun, (width-125, height-(height-50)))#sun and moon 200x200
    

    #time
    current_time = datetime.datetime.now()
    if current_time.minute-10 < 0:

        current_time_display = str(str(current_time.hour) + ':' + str(0) + str(current_time.minute))

    else:

        current_time_display = str(str(current_time.hour) + ':' + str(current_time.minute))
  
    timedisplay = golem(current_time_display, random_color, (width-200, height-(height-100)), font)
    timedisplay.KING()


   
   
    #main buttons
    if main_menu == True:
        for i in range(0, 4): 
            if i == 0:
                largebuttons = 'Gallary'
            elif i == 1:
                largebuttons = 'Characters'
            elif i == 2:
                largebuttons = 'Clubs'
            else:
                largebuttons = 'Jobs'

            large_button_width = (width/5 + i*(width/5))-150
           

            b = button(largebuttons, (large_button_width, height/2), (142,155,229), font, (200,100))
            b.createbutton()

        
            click_l = clicked(large_button_width, large_button_width+200, height/2, height/2+100)
            

            if click_l and click_value: 
               
                click_value = False
                if i == 0:
                    print('gallary')
                    
                    gallary = True
                    main_menu = False
                if i == 1:
                    print('characters')
                    
                    main_menu = False
                   
                    characters_choice = True
                if i == 2:
                    print('clubs')
                    club_choice = True
                    main_menu = False
                if i == 3:
                    print('jobs')
                    main_menu = False


        
            elif click_l and click_value == False:
                click_value = False
            else:
                click_value = True
            
        #other buttons
        for i in range(0, 3):
            if i == 0:
                smallbuttons = 'Music'
  
            elif i == 1:
                smallbuttons = 'Quit'
   
            else:
                smallbuttons = 'Options' 
 


            small_button_width = (width/3 + i*(width/5))-200

            b = button(smallbuttons, (small_button_width, height-200), (152,5,152), font, (150,75)) 
            b.createbutton()


            
            click_s = clicked(small_button_width, small_button_width+150, height-200, height-125)
           

            if click_s and click_value:
                
                click_value = False
                if i == 0:
                    print('music')
                    music = True
                    main_menu = False
                if i == 1:
                    print('quit')
                    os.remove(os.getcwd() + '\\Playlists.txt')
                    time.sleep(1)
                    playlist_create_new = open('Playlists.txt', 'w')
                    playlist_create_new.write(str(playlist))
                    playlist_create_new.close()
                    pygame.quit()
                    
                   
                    main_menu = False
                if i == 2:
                    print('options')
                    options = True
                    main_menu = False
               
            
            elif click_s and click_value == False:
                click_value = False
            else:
                click_value = True
                options = False
  
    #character choice
    if main_menu == False and characters_choice == True:
        character_return = display_characters(character_page, click_value)
       
        
        if character_return == None:
            pass

        elif character_return[0] == False:
            characters_choice = False
            characterchoice = character_return[1]
            characters = True
        
    
        if character_page < 3:
            next_page = button('Next', (width-250, height-150), sky_blue, font, (200,100))
            next_page.createbutton()
            

        if character_page != 1:
            last_page = button('Back', (50, height-150), sky_blue, font, (200,100))
            last_page.createbutton()
       

        click_c = clicked(width-250, width-50, height-150, height-50)
        click_d = clicked(50, 250, height-150, height-50)

        

        
        if (click_c or click_d) and click_value and click_frame:
            click_frame = False
            click_value = False
           
            if character_page < 3 and click_c:
                character_page += 1
            elif character_page > 1 and click_d:
                character_page -= 1
        elif (click_c or click_d) and click_value == True and click_frame == False:
            click_frame = False
            click_value = False
        
        else:
            click_frame = True
            click_value = True


    else:
        characters_choice = False

    #character display
    if main_menu == False and characters == False and manage_playlist == False:

        back_button = button('Back', (width-(width-50), height-(height-50)), (0,207,255), font, (200,100))
        back_button.createbutton()
        click_b = clicked(width-(width-50), width-(width-250), height-(height-50), height-(height-150))

        if click_b and click_value:
            main_menu = True
            click_value = False
                
        elif click_b and click_value == False:

            click_value = False

        else:

            click_value = True

    #back button from character display
    if main_menu == False and characters == True:

        back_button = button('Back to', (width-(width-260), height-(height-50)), (0,207,255), font, (200,100))
        back_button.createbutton()
        click_b = clicked(width-(width-260), width-(width-460), height-(height-50), height-(height-150))

        if click_b and click_value:
  
            characters_choice = True
            click_value = False
            characters = False
                
        elif click_b and click_value == False:

            click_value = False

        else:

            click_value = True
    else:
        characters = False


    #stop slideshow
    if pygame.mouse.get_pressed()[0]:
            stop_slideshow = True
    

    #gallary and slideshow
    if main_menu == False and gallary == True:
        gallary_button = button('Slideshow', (width-300, height-(height-200)), sky_blue, font, (200,100))
        gallary_button.createbutton()

        click_g = clicked(width-300, width-100, height-(height-200), height-(height-300))

        if click_g and click_value:
            slideshow = True
            stop_slideshow = False
            click_value = False
                
        elif click_g and click_value == False:

            click_value = False

        else:

            click_value = True

    else:
        gallary = False


    #slideshow    
    if slideshow and stop_slideshow == False:
        

     
        iamatarabullprogrammer=github(timer_69,random_image,timer_max)
        timer_69=iamatarabullprogrammer[0]
        random_image=iamatarabullprogrammer[1]
    
    #clubs
    
    if club_choice and main_menu == False:
        for x in range(3):
            
            if not x == 2:
                club_number = 3
            else:
                club_number = 1
            for i in range(club_number):
                if not x == 2:
                    club_display_width = width/6 + i*width/4
                    club_display_height = height/4 + x*height/2
                    club_display_color = sky_blue
                else:
                    club_display_width = width/2-160
                    club_display_height = height/2
                    club_display_color = gold
                club_display = button(list_clubs[i+(3*x-1)], (club_display_width, club_display_height), club_display_color, font, (300,100))
                club_display.createbutton()
    else:
        club_choice = False

    #clubs = True
    clubs = False
    #main_menu = False
    if clubs: #and main_menu != True:

        
        
        clubs_display.create_club_display()

    else:
        clubs = False
        

#pop so it returns what you removed


    

    #music
    if music and main_menu == False:
        '''
        if len(playlist_keys):

        try:
            playlist_name = button(str(playlist_keys[playlist_choice]), (width-500, 180), (0,0,102), font, (400,70), cyan)

            playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)
        except IndexError:
            print('king')
            playlist_name = button('You Have No Playlists', (width-500, 180), (0,0,102), font, (400,70), cyan)

            playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), [], [400,100], font, 102)
        '''

        #playlists and repeats

        playlist_name.createbutton() 

        #print(str(sum(music_length(playlist[playlist_keys[playlist_choice[x]]] for x in range(len(playlist[playlist_keys[playlist_choice]]))))))

        #print(music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][1])+'.mp3'))

        #print(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))]))

        #print('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][0])+'.mp3')

        #print(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)))

        #playlist_duration_button = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)
        
        #playlist_duration_button = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)

        
        


        playlist_duration.createbutton()      

        playlist_box_display.displaybuttons() 
       
        repeat_button_1.createbutton()
        repeat_button_2.createbutton()
        repeat_title.KING()
        if pygame.mixer.music.get_busy() == 1:
            clicked_r = clicked(width-150, width-50, height-150, height-50)
            if repeat_thing:
                if clicked_r and repeat == False:
                    repeat = True
                elif clicked_r and repeat == True:
                    repeat = False
            
            if repeat and pygame.mouse.get_pressed()[0] == 1:
                repeat_thing = False
            elif repeat == False and pygame.mouse.get_pressed()[0] == 1:
                repeat_thing = False
            else:
                repeat_thing = True
        if repeat:
            screen.blit(checkmark, (width-125, height-125))

        checkbox((200, height-125), (0,0,102), redblue, 'Shuffle', red, shuffle)
        clicked_s = clicked(200, 300, height-125, height-25)
        #print(clicked_s)
        if shuffle_thing:
            if clicked_s and shuffle == False:
                shuffle = True
                shuffle_playlist = False
            elif clicked_s and shuffle == True:
                shuffle = False
        
        if shuffle and pygame.mouse.get_pressed()[0] == 1:
            shuffle_thing = False
        elif shuffle == False and pygame.mouse.get_pressed()[0] == 1:
            shuffle_thing = False
        else:
            shuffle_thing = True
        checkbox((width-625, height-220), (0,0,102), sky_blue, 'Shuffle', red, shuffle_playlist)
        clicked_p = clicked(width-625, width-525, height-220, height-120)
        #print(clicked_s)
        if shuffle_playlist_thing:
            if clicked_p and shuffle_playlist == False:
                shuffle_playlist = True
                shuffle = False
            elif clicked_p and shuffle_playlist == True:
                shuffle_playlist = False
        
        if shuffle_playlist and pygame.mouse.get_pressed()[0] == 1:
            shuffle_playlist_thing = False
        elif shuffle_playlist == False and pygame.mouse.get_pressed()[0] == 1:
            shuffle_playlist_thing = False
        else:
            shuffle_playlist_thing = True
        music_box.displaybuttons()
        music_box_title.createbutton()
        #print(shuffle_playlist, shuffle_playlist_thing)
        screen.blit(toad, (width/2-int(607/3)+40, height/2-int(718/3)))
        screen.blit(treble, (50, 190))
        screen.blit(bass, (400,190))

        #next and back buttons
        
        if playlist_choice < len(playlist_keys)-1 and len(playlist_keys) != 1:
            next_page = button('Next', (width-290, height-200), sky_blue, font, (100,50))
            next_page.createbutton()
            
        

        if  playlist_choice != 0:
            last_page = button('Back', (width-490, height-200), sky_blue, font, (100,50))
            last_page.createbutton()
       

        click_c = clicked(width-290, width-190, height-200, height-150)
        click_d = clicked(width-490, width-390, height-200, height-150)

    
        if (click_c or click_d) and click_value and click_frame:
            click_frame = False
            click_value = False
            if playlist_choice < len(playlist_keys)-1 and click_c:
                playlist_choice += 1
                playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)
                playlist_name = button(str(playlist_keys[playlist_choice]), (width-500, 150), (0,0,102), font, (400,70), cyan)
                playlist_duration = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/3600))+":"+"0"*(2-len(str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))))+str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)
            elif playlist_choice > 0 and click_d:
                playlist_choice -= 1
                playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)
                playlist_name = button(str(playlist_keys[playlist_choice]), (width-500, 150), (0,0,102), font, (400,70), cyan)
                playlist_duration = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/3600))+":"+"0"*(2-len(str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))))+str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)

        elif (click_c or click_d) and click_value == True and click_frame == False:
            click_frame = False
            click_value = False
        
        else:
            click_frame = True
            click_value = True

        manage_playlist_button = button('Manage Playlists', (width-550, height-100), (0,0,102), font, (350,50), cyan)
        manage_playlist_button.createbutton()

        clicked_p = clicked(width-550, width-200, height-100, height-50)

        if clicked_p:
            manage_playlist = True
            music = False

    else:
        music = False

    if manage_playlist and main_menu == False:
        back_button = button('Back to', (width-(width-260), height-(height-50)), (0,207,255), font, (200,100))
        back_button.createbutton()
        #try:
            #indexfunction(index4, playlist_manage_box_display_options, music_list, indexlist = returnindices(playlist[playlist_keys[playlist_manage_choice]], music_list))
        #except NameError:
            #pass
        click_b = clicked(width-(width-260), width-(width-460), height-(height-50), height-(height-150))

        if click_b:
            manage_playlist = False
            music = True

    
        if playlist_create_new_error == True:
            if playlist_create_timer < 1:
                playlist_new_error.KING()
                playlist_create_timer += 0.01
            else:
                playlist_create_new_error = False    
                playlist_create_timer = 0
        playlist_manage_title.KING()
        playlist_manage_box_display.displaybuttons()
        playlist_manage_box_display_options_create_new.createbutton()

        click_n = clicked(width-500, width-100, height-100, height-20)
        #try:
            #create_playlist(playlist_input_text)
        #except NameError:
            #pass
        #print(playlist_new_name)

        if playlist_create == True:
            playlist_manage_box_display_options_create_new = button(playlist_new_name, (width-500, height-100), (0,0,102), font, (400,80), cyan)
            click_p = clicked(0, width, 0, height)
            if click_p:
                if pygame.mouse.get_pos()[0] > width-500 and pygame.mouse.get_pos()[0] < width-100 and pygame.mouse.get_pos()[1] > height-100 and pygame.mouse.get_pos()[1] < height-20:
                    pass
                else:
                    playlist_new_name = ''
                    playlist_create = False
        else:
            playlist_manage_box_display_options_create_new = button('Create New', (width-500, height-100), (0,0,102), font, (400,80), cyan)

        if pygame.mouse.get_pressed()[0]== False:
            playlist_click_up = True
        if click_n and playlist_click_up:
            
            
            #playlist_new_name = create_playlist()
            
            #show what songs are in the playlist
            '''
            if playlist_new_name in playlist:
                playlist_create = False
                #print('golem')
                pass
            else:
            '''
            playlist_create = True
                
                #create_playlist()
                #print('king')
                
        
        

        if len(playlist_keys) != 0:
            playlist_manage_box_display_options_delete.createbutton()
            click_r = clicked(width-500, width-100, height-200, height-120)
            if click_r:
                #print('delete')
                try:
                    playlist.pop(playlist_keys[playlist_manage_choice], None)
                    playlist_keys.remove(playlist_keys[playlist_manage_choice])
                    playlist_manage_box_display = buttontextbox(screen, pygame.Rect(100, 250, 400, 600), playlist_keys, [400,100], font, 102)

                    #print(len(playlist_keys))
                    if len(playlist_keys) != 0:
                        if playlist_choice == playlist_manage_choice:
                            playlist_choice -=1
                        playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), playlist[playlist_keys[playlist_choice]], [400,100], font, 102)
                        playlist_name = button(str(playlist_keys[playlist_choice]), (width-500, 150), (0,0,102), font, (400,70), cyan)
                        playlist_duration = button('Duration: '+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/3600))+":"+"0"*(2-len(str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))))+str(int((sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])/60)%60))+":"+"0"*(2-len(str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60))))+str(int(sum([music_length('Sounds/Music/'+str(playlist[playlist_keys[playlist_choice]][x])+'.mp3') for x in range(len(playlist[playlist_keys[playlist_choice]]))])%60)), (width-500, 210), (0,0,102), font3, (400,40), redblue)
                        playlist_manage_title = golem('Manage Playlists', cyan, (300,200), font)
                        #integrate pause button
                        #fix bug of deleting playlist1 while on it making the playlist 2 have a back button maybe by fixing when it updates or only doing back when len(playlist_keys) is > 1 or something
                        #make click stuff more optimized by isntead of doing click_xxf = clicked() make it so click = clicked() and clicked will return True or False so only one click variable and make it if its true locally inside the function return True else return False
                        
                    else:
                        playlist_box_display = buttontextbox(screen, pygame.Rect(width-500, 250, 400, 600), [], [400,100], font, 102)
                        playlist_name = button('You Have No Playlists', (width-500, 150), (0,0,102), font, (400,70), cyan)
                        playlist_duration = button('', (width-150, 220), (0,0,102), font, (400,30), cyan)
                        playlist_manage_title = golem('Create a New Playlist to Manage', cyan, (300,200), font)
                        

                    playlist_manage_choice = ''
                    
                except TypeError:
                    pass
                except NameError:
                    pass
        


        try:
            #print(playlist)
            #print(playlist_manage_choice)
            playlist_manage_choice = playlist_manage_choice
            if len(playlist_keys) != 0:
                       
                playlist_manage_box_display_options.displaybuttons()
                
                playlist_manage_box_display_options_title.KING()
                
            

            #put in for loop with mousebuttondown

            

            

            
            
                #print(playlist_manage_choice, playlist)
                #176
            #playlist_manage_title = golem('Manage Playlists', cyan, (300,200), font)

        except NameError:
            #playlist_manage_title = golem('Create a New Playlist to Manage', cyan, (300,200), font)
            pass
       
        
    

        
    else:
        manage_playlist = False
        playlist_click_up = False
        try:
            del(playlist_manage_choice)
        except NameError:
            pass
    #print(playlist_choice, playlist_create)

    #options
    if options and main_menu == False:
        for x in range(1,4): #about(world information, dates, minecraft copyright, program information like lines of code idk), controls, github page and maybe other social pages
            if x == 1:
                options_text = 'About'
            elif x == 2:
                options_text = 'Controls'
            else:
                options_text = 'Github'



            main_options_box_height = x*(1080/4)-50

            main_options_box = button(options_text,  (width/2-150, main_options_box_height), (165,132,192) , font, (300, 100))

            main_options_box.createbutton()

            click_soc = clicked(width/2-150, width/2+150, main_options_box_height, main_options_box_height+100)

           
           
          
            
            if click_soc and click_value: 

                click_value = False
                if x == 1:
                    print('about')
                    options = False
                    about = True
               
                elif x == 2:
                    print('controls')
                    options = False
                    controls = True
               
                elif x == 3:
                    opengithub()
                    
                

                        
               
    
            elif click_soc and click_value == False:
                click_value = False

            else:
                click_value = True
          

  
    #patch notes
    if main_menu and screen.get_width() == 1920:
        patchnotes_display.display()
   
    

    if about and main_menu == False:
        #credids make a loop that blits a large height box with credits more and more upwards like in the movies or video games
        #information box on one of the corners
        #information includes how long it toke when it aobut started and finished and how long toke stuff like that king
        #add slider function
        #make a photo slider so it changes the x value in relation to the slider
        #for x in range(3):
            #about_information = button(information[x], (width-350, height-(x*100+150)), sky_blue, font2, (300,100), gold)
            #about_information.createbutton_color()
        about_information.display()
        other_information_display.display()
        credits_display.display()
        #ravager_credits_display = button('Credits', (width-350, height-500), cyan, font, (300,100), red)
        #ravager_credits_display.createbutton_color()

        clicked_c = clicked(width-350, width-50, height-500, height-400)

        if clicked_c and click_value:

            display_credits = True
                
            
        
        elif click_c and click_value == False:
            click_value = False

        else:
            click_value = True
        
    else:
        about = False

    if display_credits:
  
        if pygame.mouse.get_pressed()[0] == False:
            about = False

        if about == False:
            for x in range(1000):
                credits_height = x
                credits_height_2 = x+height
                credits_display = button('king', (0,credits_height), sky_blue, font, (width,height))
                credits_display.createbutton()
                credits_display = button('king', (0, credits_height_2), gold, font, (width, height))
                credits_display.createbutton()
                if pygame.mouse.get_pressed()[0]:
                    about = True
                    display_credits = False
        '''
        print(credits_click)
        
        about = False
        
        if pygame.mouse.get_pressed()[0] == False:
            credits_click = True
            display_credits = False
            about = True   
        if pygame.mouse.get_pressed()[0] and credits_click == True:
            about = True
            display_credits = False
        '''
    #static updates text
    if main_menu:
        patchnotes_static_text = button('Updates', (width-(width-50),height-350), sky_blue, font2, (350,25))
        patchnotes_static_text.createbutton()
    if music:
        if (music_box.beingclicked):
            music_box.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)
        if (playlist_box_display.beingclicked):
            playlist_box_display.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)
 
    if manage_playlist:
        if (playlist_manage_box_display.beingclicked):
            playlist_manage_box_display.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)
        if (playlist_manage_box_display_options.beingclicked):
            playlist_manage_box_display_options.dragscroll(pygame.mouse.get_pos()[1]-startmouseposition)

    startmouseposition=pygame.mouse.get_pos()[1]
    
    title = get_title(gallary, characters_choice, characters, club_choice, options, music, characterchoice)

    title_display = golem(title, (3, 254, 155), (width/2, 180), font)

    title_display.KING()

    music_bar_return = music_bar_display((width/2-250, height-30), (0,0,102), cyan, (500,25), music_length(music_playing), scroll_bar_size, music_bar_click, seconds)
    
    seconds = 0

    scroll_bar_size = music_bar_return[0]

    music_bar_click = music_bar_return[1]

    seconds = music_bar_return[2]

    #print(seconds/1000)

 


























































































    clock.tick(144)

    
    pygame.display.flip()
