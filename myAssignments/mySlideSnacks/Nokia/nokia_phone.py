from rock_paper_scissor import play_rock_paper_scissor
running = True;
while running: 
	main_menu = """
	==== Nokia 3310 Main menu ====
		1. PhoneBook 
		2. Messages
		3. Chat
		4. Call register
		5. Tones
		6. Settings
		7. Call divert
		8. Games
		9. Calculator
		10. Reminders
		11. Clock
		12. Profiles
		13. Sim services
		
			00 Turn Off Handheld device
		       """

	print(main_menu)
	
	users_choice = input("Choose an option: ")
	match users_choice:
		case "1":
			in_phone_book = True
			while in_phone_book:
				print("""

				=== Phone book ===
				1. Search
				2. Service Nos
				3. Add name
				4. Erase 
				5. Edit				 	
				6. Assign tone
				7. Send b'card
				8. Options
				   1. Type of view
				   2. Memory Status
				9. Speed dials
				10. Voice tags
				
					press 00 --> Back 
				   """)	
				users_choice_phone_book = input("Choose an option: ")
				match users_choice_phone_book:
					case "1":
						print("""
				=== Opening search box ===""")
						in_searching = True
						while in_searching:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_searching = False
								case _:
									print("Invalid Input")
									continue

					case "2":
						print("""
				=== Opening service numbers ===
						


					press 00 <--Back
						""")
						in_service_nos = True
						while in_service_nos:
							users_choice_service_nos = input("Choose an option: ")	
							match users_choice_service_nos:
								case "00":
									in_service_nos = False
								case _:
									print("Invalid Input")
									continue
					case "3": 
						print("""
				=== Add names here === """)
						in_add_name = True
						while in_add_name:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_add_name = False
								case _:
									print("Invalid Input")
									continue
					case "4": 
						print("""
				=== Erase here === """)
						in_erase_menu = True
						while in_erase_menu:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_erase_menu = False
								case _:
									print("Invalid Input")
									continue
					case "5": 
						print("""
				==== Edit Here ==== """)
						in_edit_menu = True
						while in_edit_menu:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_edit_menu = False
								case _:
									print("Invalid Input")
									continue
					case "6": 
						print("""
				=== Assign Tunes Here === """)
						assign_tune_menu = True
						while assign_tune_menu:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									assign_tune_menu = False
								case _:
									print("Invalid Input")
									continue
					case "7": 
						print("""
				=== Send b'card === """)
						in_send_b_card_menu = True
						while in_send_b_card_menu:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_send_b_card_menu = False
								case _:
									print("Invalid Input")
									continue
					case "8":
						in_options_menu = True
						while in_options_menu:
							print("""
				=== Options ===

				1. Type of view
				2. Memory status
				
				<-- 00 Back
							""")
										
							users_choice_options = input("Choose an option: ")
							match users_choice_options:
								case "1": 
									print("""
				=== Change Type of View Here === """)
									in_type_of_view = True
									while in_type_of_view:
										print("""
					00 <-- Back
				    			 			""")
										users_choice_type_of_view = input("Choose an option: ")
										match users_choice_type_of_view:
											case "00":
												in_type_of_view = False
											case _:
												print("Invalid Input")
												continue

								case "2": 
									print("""
				=== Check Memory Status Here === """)
									in_memory_status = True
									while in_memory_status:
										print("""
					00 <-- Back
				    			 			""")
										users_choice_memory_status = input("Choose an option: ")
										match users_choice_memory_status:
											case "00":
												in_memory_status = False
											case _:
												print("Invalid Input")
												continue

								case "00":
									in_options_menu = False
								case _:
									print("Invalid Input")
									continue

					case "9": 
						print("""
				=== Speed Dial Numbers === """)
						in_speed_dial_menu = True
						while in_speed_dial_menu:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_speed_dial_menu = False
								case _:
									print("Invalid Input")
									continue
					case "10": 
						print("""
				=== Set Your Voice Tags Here === """)
						in_speed_dial_menu = True
						while in_speed_dial_menu:
							print("""
					00 <-- Back
				    			 """)
							users_choice_phone_book = input("Choose an option: ")
							match users_choice_phone_book:
								case "00":
									in_speed_dial_menu = False
								case _:
									print("Invalid Input")
									continue

					case "00":
						in_phone_book = False
					case _:
						print("Invalid Input")
						continue
		case "2": 
			print(""" 
			=== Messages===
			""")
			in_message_menu = True
			while in_message_menu:
				print("""
			1. Write messages
			2. Inbox
			3. Outbox
			4. Picture messages
			5. Templates
			6. Smileys
			7. Message settings
			8. Info Service
			9. Voice mailbox number
			10. Service command editor

				<-- 00 Back
				""")
				users_choice_phone_book = input("Choose an option: ")
				match users_choice_phone_book:
					case "1":
						print("""
			=== Write Messages Here === """)
						in_write_messages = True
						while in_write_messages:
							print("""
				00 <-- Back
				    			 """)
							users_choice_write_messages = input("Choose an option: ")
							match users_choice_write_messages:
								case "00":
									in_write_messages = False
								case _:
									print("Invalid Input")
									continue
					case "2":
						print("""
			=== Check Inbox Here === """)
						in_inbox = True
						while in_inbox:
							print("""
				00 <-- Back
				    			 """)
							users_choice_inbox = input("Choose an option: ")
							match users_choice_inbox:
								case "00":
									in_inbox = False
								case _:
									print("Invalid Input")
									continue
					case "3":
						print("""
			=== Check Outbox Here === """)
						in_outbox = True
						while in_outbox:
							print("""
				00 <-- Back
				    			 """)
							users_choice_outbox = input("Choose an option: ")
							match users_choice_outbox:
								case "00":
									in_outbox = False
								case _:
									print("Invalid Input")
									continue
					case "4":
						print("""
			=== View Picture Messages Here === """)
						in_picture_messages = True
						while in_picture_messages:
							print("""
				00 <-- Back
				    			 """)
							users_choice_picture_messages = input("Choose an option: ")
							match users_choice_picture_messages:
								case "00":
									in_picture_messages = False
								case _:
									print("Invalid Input")
									continue

					case "5":
						print("""
			=== Set Templates Here === """)
						in_templates = True
						while in_templates:
							print("""
				00 <-- Back
				    			 """)
							users_choice_templates = input("Choose an option: ")
							match users_choice_templates:
								case "00":
									in_templates = False
								case _:
									print("Invalid Input")
									continue
					case "6":
						print("""
			=== Choose Smileys Here === """)
						in_smileys = True
						while in_smileys:
							print("""
				00 <-- Back
				    			 """)
							users_choice_smileys= input("Choose an option: ")
							match users_choice_smileys:
								case "00":
									in_smileys = False
								case _:
									print("Invalid Input")
									continue
					case "7":
						print("""
			=== Message Settings ===
						""")
						in_message_settings = True
						while in_message_settings:
							print("""
			1. Set 1
			

			2. Commons

				00 <-- Back
							""")
							users_message_settings = input("Choose an option: ")
							match users_message_settings:
								case "1":
									print("""
			=== Set 1 === 
									""")
									in_set_1 = True
									while in_set_1:
										print("""
			1. Message center number
			2. Messages sent as
			3. Message validity

				<-- 00 Back
										""")
										users_message_center_number = input("Choose an option: ")
										match users_message_center_number:
											case "1":
												print("""
			=== View Message Center Here  === """)
												in_message_center = True
												while in_message_center:
													print("""
				00 <-- Back
				    								""")
													users_choice_message_center = input("Choose an option: ")
													match users_choice_message_center:
														case "00":
															in_message_center = False
														case _:
															print("Invalid Input")
															continue 
											case "2":
												print("""
			=== Messages Sent As  === """)
												in_message_sent_as = True
												while in_message_sent_as:
													print("""
				00 <-- Back
				    								""")
													users_choice_message_sent_as = input("Choose an option: ")
													match users_choice_message_sent_as:
														case "00":
															in_message_sent_as = False
														case _:
															print("Invalid Input")
															continue
											case "2":
												print("""
			=== Check Message Validity Here  === """)
												in_message_validity = True
												while in_message_validity:
													print("""
				00 <-- Back
				    								""")
													users_choice_message_validity = input("Choose an option: ")
													match users_choice_message_validity:
														case "00":
															in_message_validity = False
														case _:
															print("Invalid Input")
															continue	
																		
											case "00":
												in_set_1 = False
											case _:
												print("Invalid Input")
												continue
			
								#here
								case "2":
									print("""
			=== Common === 
									""")
									in_common = True
									while in_common:
										print("""
			1. Delivery report
			2. Reply via same centre
			3. Character support

				<-- 00 Back
										""")
										users_common = input("Choose an option: ")
										match users_common:
											case "1":
												print("""
			=== View Delivery Report Here  === """)
												in_delivery_report = True
												while in_delivery_report:
													print("""
				00 <-- Back
				    								""")
													users_choice_delivery_report = input("Choose an option: ")
													match users_choice_delivery_report:
														case "00":
															in_delivery_report = False
														case _:
															print("Invalid Input")
															continue 
											case "2":
												print("""
			=== Reply via same centre === """)
												in_reply_centre = True
												while in_reply_centre:
													print("""
				00 <-- Back
				    								""")
													users_choice_reply_centre = input("Choose an option: ")
													match users_choice_reply_centre :
														case "00":
															in_reply_centre = False
														case _:
															print("Invalid Input")
															continue
											case "3":
												print("""
			=== Check Character Support Here === """)
												in_character_support = True
												while in_character_support:
													print("""
				00 <-- Back
				    								""")
													users_choice_character_support = input("Choose an option: ")
													match users_choice_character_support:
														case "00":
															in_character_support = False
														case _:
															print("Invalid Input")
															continue	
																		
											case "00":
												in_common = False
											case _:
												print("Invalid Input")
												continue
 
			

								case "00":
									in_message_settings = False
								case _:
									print("Invalid Input")
									continue
					case "8":
						print("""
			=== View Info Service Here === """)
						in_info_service = True
						while in_info_service:
							print("""
				00 <-- Back
				    			 """)
							users_choice_info_servie= input("Choose an option: ")
							match users_choice_info_servie:
								case "00":
									in_info_service = False
								case _:
									print("Invalid Input")
									continue 
					case "9":
						print("""
			=== View Voice MailBox Numbers Here === """)
						in_voice_mailbox = True
						while in_voice_mailbox:
							print("""
				00 <-- Back
				    			 """)
							users_choice_info_service= input("Choose an option: ")
							match users_choice_info_service:
								case "00":
									in_voice_mailbox = False
								case _:
									print("Invalid Input")
									continue
					case "10":
						print("""
			=== View Service Command Editor Here === """)
						in_service_editor = True
						while in_service_editor:
							print("""
				00 <-- Back
				    			 """)
							users_choice_service_editor = input("Choose an option: ")
							match users_choice_service_editor:
								case "00":
									in_service_editor = False
								case _:
									print("Invalid Input")
									continue

					case "00":
						in_message_menu = False
					case _:
						print("Invalid Input")
						continue	
		case "3":
			print("""
			=== View Chat Here === """)
			in_chat = True
			while in_chat:
				print("""
				00 <-- Back
				 """)
				users_choice_chat = input("Choose an option: ")
				match users_choice_chat:
					case "00":
						in_chat = False
					case _:
						print("Invalid Input")
						continue
		case "4":
			print("""
			
			=== Call Register ===
			""")
			in_call_register = True
			while in_call_register:
				print("""
	
				1. Missed Calls
				2. Recieved Calls
				3. Dialled Numbers
				4. Erase recent calls lists
				5. Show call duration
				6. Show all costs
				7. Call cost settings
				8. Prepaid credit

					<--00 Back
					""")
				users_choice_call_register = input("Choose an option: ")
				match users_choice_call_register:
					case "1":
						print("""
			=== View Missed Calls Here === """)
						in_missed_calls = True
						while in_missed_calls :
							print("""
				00 <-- Back
				 			""")
							users_choice_missed_calls = input("Choose an option: ")
							match users_choice_missed_calls:
								case "00":
									in_missed_calls  = False
								case _:
									print("Invalid Input")
									continue
					case "2":
						print("""
			=== View Recieved Calls Here === """)
						in_recieved_calls = True
						while in_recieved_calls :
							print("""
				00 <-- Back
				 			""")
							users_choice_recieved_calls = input("Choose an option: ")
							match users_choice_recieved_calls:
								case "00":
									in_recieved_calls  = False
								case _:
									print("Invalid Input")
									continue
					case "3":
						print("""
			=== View Dialled numbers Here === """)
						in_dialled_numbers = True
						while in_dialled_numbers :
							print("""
				00 <-- Back
				 			""")
							users_choice_dialled_numbers = input("Choose an option: ")
							match users_choice_dialled_numbers :
								case "00":
									in_dialled_numbers  = False
								case _:
									print("Invalid Input")
									continue
					case "4":
						print("""
			=== Erase Recent Call List Here === """)
						in_call_list = True
						while in_call_list:
							print("""
				00 <-- Back
				 			""")
							users_choice_call_list = input("Choose an option: ")
							match users_choice_call_list :
								case "00":
									in_call_list  = False
								case _:
									print("Invalid Input")
									continue
					case "5":
						print("""
			=== Show Call Duration === """)
						in_call_duration = True
						while in_call_duration:
							print("""
			
			1. Last call duration
			2. All calls' duration
			3. Recieved calls' duration
			4. Dialled calls' duration
			5. Clear timers 

				<-- 00.Back
				""")
							users_choice_in_call_duration = input("Choose an option: ")
							match users_choice_in_call_duration: 
								case "1":
									print("""
			=== Check Last Call Duration Here === """)
									in_last_call_duration = True
									while in_last_call_duration:
										print("""
				00 <-- Back
				 						""")
										users_choice_last_call_duration = input("Choose an option: ")
										match users_choice_last_call_duration :
											case "00":
												in_last_call_duration  = False
											case _:
												print("Invalid Input")
												continue
								case "2":
									print("""
			=== Check All Calls' Duration Here === """)
									in_all_call_duration = True
									while in_all_call_duration:
										print("""
				00 <-- Back
				 						""")
										users_choice_last_all_call_duration = input("Choose an option: ")
										match users_choice_last_all_call_duration :
											case "00":
												in_all_call_duration = False
											case _:
												print("Invalid Input")
												continue
								case "3":
									print("""
			=== Check Recieved Calls' Duration Here === """)
									in_recieved_call_duration = True
									while in_recieved_call_duration:
										print("""
				00 <-- Back
				 						""")
										users_choice_recieved_call_duration = input("Choose an option: ")
										match users_choice_recieved_call_duration :
											case "00":
												in_recieved_call_duration = False
											case _:
												print("Invalid Input")
												continue
								case "4":
									print("""
			=== Check Dialled Calls' Duration Here === """)
									in_dialled_call_duration = True
									while in_dialled_call_duration:
										print("""
				00 <-- Back
				 						""")
										users_choice_dialled_call_duration = input("Choose an option: ")
										match users_choice_dialled_call_duration :
											case "00":
												in_dialled_call_duration = False
											case _:
												print("Invalid Input")
												continue
								case "5":
									print("""
			=== Clear Timers Here === """)
									in_clear_timers = True
									while in_clear_timers:
										print("""
				00 <-- Back
				 						""")
										users_choice_clear_timers = input("Choose an option: ")
										match users_choice_clear_timers :
											case "00":
												in_clear_timers = False
											case _:
												print("Invalid Input")
												continue
								

								case "00": 
									in_call_duration = False
								case _:
									print("Invalid Input")
									continue
					case "6":
									print("""
			=== View Call Costs Here === """)
									in_show_all_costs= True
									while in_show_all_costs:
										print("""
			1. Last Call Cost
			2. All calls' cost 
			3. Clear counters

	
				<--00 Back			
										""")
										users_choice_show_all_costs = input("Choose an option: ")
										match users_choice_show_all_costs:
											case "1":
												print("""
			=== Check Last Call Cost Here === """)
												in_last_call_cost = True
												while in_last_call_cost:
													print("""
				00 <-- Back
				 									""")
													users_choice_dialled_call_duration = input("Choose an option: ")
													match users_choice_dialled_call_duration :
														case "00":
															in_last_call_cost = False
														case _:
															print("Invalid Input")
															continue
											case "2":
												print("""
			=== Check All Calls' Cost Here === """)
												in_all_call_cost = True
												while in_all_call_cost:
													print("""
				00 <-- Back
				 									""")
													users_choice_all_call_cost = input("Choose an option: ")
													match users_choice_all_call_cost :
														case "00":
															in_all_call_cost = False
														case _:
															print("Invalid Input")
															continue
											case "3":
												print("""
			=== Clear Counters Here === """)
												in_clear_counters = True
												while in_clear_counters:
													print("""
				00 <-- Back
				 									""")
													users_choice_clear_counters = input("Choose an option: ")
													match users_choice_clear_counters :
														case "00":
															in_clear_counters = False
														case _:
															print("Invalid Input")
															continue
											case "00":
												in_show_all_costs = False
											case _:
												print("Invalid Input")
												continue 
					case "7":
									print("""
			=== Review Call Costs Settings Here === """)
									in_call_costs_settings = True
									while in_call_costs_settings:
										print("""
			1. Call Cost limit
			2. Show cost in
 
				<-- 00. Back
				
										""")
										users_choice_call_costs_settings = input("Choose an option: ")
										match users_choice_call_costs_settings:
											case "1":
												print("""
			=== Adjust Call Cost Limit Here === """)
												in_call_cost_limit = True
												while in_call_cost_limit:
													print("""
				00 <-- Back
				 									""")
													users_choice_call_cost_limit = input("Choose an option: ")
													match users_choice_call_cost_limit :
														case "00":
															in_call_cost_limit = False
														case _:
															print("Invalid Input")
															continue
											case "2":
												print("""
			=== Show Cost In === """)
												in_show_cost_in = True
												while in_show_cost_in:
													print("""
				00 <-- Back
				 									""")
													users_choice_show_cost_in = input("Choose an option: ")
													match users_choice_show_cost_in :
														case "00":
															in_show_cost_in = False
														case _:
															print("Invalid Input")
															continue
											case "00":
												in_call_costs_settings = False
					case "8":
						print("""
			=== Set Prepaid Credit Here === """)
						in_prepaid_credit = True
						while in_prepaid_credit:
							print("""
				00 <-- Back
				 			""")
							users_choice_prepaid_credit = input("Choose an option: ")
							match users_choice_prepaid_credit :
								case "00":
									in_prepaid_credit  = False
								case _:
									print("Invalid Input")
									continue


												

					case "00":
						in_call_register = False
					case _:
						print("Invalid Input")
						continue
	
		case "5": 
			in_tones = True
			while in_tones:
				print("""
			
			=== Tones === 
			1. Ringing Tones		
			2. Ringing Volume
			3. Incoming call alert
			4. Composer
			5. Message alert tunes
			6. Keypad Tones
			7. Warning and game tones
			8. Vibrating alert 
			9. Screen Saver

				<-- 00. Back		
			""")
				users_choice_prepaid_credit = input("Choose an option: ")
				match users_choice_prepaid_credit :
					case "1":
						print("""
			=== Set Ringing Tone Here === """)
						in_ringing_tone = True
						while in_ringing_tone:
							print("""


				00 <-- Back
				 			""")
							users_choice_ringing_tone = input("Choose an option: ")
							match users_choice_ringing_tone:
								case "00":
									in_ringing_tone  = False
								case _:
									print("Invalid Input")
									continue
					case "2":
						print("""
			=== Set Ringing Tone Here === """)
						in_ringing_tone = True
						while in_ringing_tone:
							print("""


				00 <-- Back
				 			""")
							users_choice_ringing_tone = input("Choose an option: ")
							match users_choice_ringing_tone:
								case "00":
									in_ringing_tone  = False
								case _:
									print("Invalid Input")
									continue
					case "3":
						print("""
			=== Set Incoming Call Alerts Here === """)
						in_incoming_calls = True
						while in_incoming_calls:
							print("""


				00 <-- Back
				 			""")
							users_choice_incoming_calls = input("Choose an option: ")
							match users_choice_incoming_calls:
								case "00":
									in_incoming_calls  = False
								case _:
									print("Invalid Input")
									continue
					case "4":
						print("""
			=== Composer === """)
						in_composer = True
						while in_composer:
							print("""


				00 <-- Back
				 			""")
							users_choice_composer = input("Choose an option: ")
							match users_choice_composer:
								case "00":
									in_composer  = False
								case _:
									print("Invalid Input")
									continue
					case "5":
						print("""
			=== Set Message Alerts Here === """)
						in_message_alert = True
						while in_message_alert:
							print("""


				00 <-- Back
				 			""")
							users_choice_message_alert = input("Choose an option: ")
							match users_choice_message_alert:
								case "00":
									in_message_alert  = False
								case _:
									print("Invalid Input")
									continue
					case "6":
						print("""
			=== Set Key Pad Tones Here === """)
						in_key_pad_tone = True
						while in_key_pad_tone:
							print("""


				00 <-- Back
				 			""")
							users_choice_key_pad_tone = input("Choose an option: ")
							match users_choice_key_pad_tone:
								case "00":
									in_key_pad_tone  = False
								case _:
									print("Invalid Input")
									continue
					case "7":
						print("""
			=== Set Warning and Game Tones Here === """)
						in_warning_and_game_tone = True
						while in_warning_and_game_tone:
							print("""


				00 <-- Back
				 			""")
							users_choice_warning_and_game_tone = input("Choose an option: ")
							match users_choice_warning_and_game_tone:
								case "00":
									in_warning_and_game_tone  = False
								case _:
									print("Invalid Input")
									continue
					case "8":
						print("""
			=== Set Vibrate Alert Here === """)
						in_vibrate_alert = True
						while in_vibrate_alert:
							print("""


				00 <-- Back
				 			""")
							users_choice_vibrate_alert = input("Choose an option: ")
							match users_choice_vibrate_alert:
								case "00":
									in_vibrate_alert  = False
								case _:
									print("Invalid Input")
									continue
					case "9":
						print("""
			=== Set Screen Saver Here === """)
						in_screen_saver = True
						while in_screen_saver:
							print("""


				00 <-- Back
				 			""")
							users_choice_screen_saver = input("Choose an option: ")
							match users_choice_screen_saver:
								case "00":
									in_screen_saver  = False
								case _:
									print("Invalid Input")
									continue					
					
					case "00":
						in_tones  = False
					case _:
						print("Invalid Input")
						continue
					


		case "6":
			print("""
			=== Settings === 
			""") 
			in_settings = True
			while in_settings:
				print("""
			1. Call settings
			2. Phone Settings
			3. Security settings
			4. Restore factory settings
	
				<-- 00. Back 
				""")
				users_choice_screen_saver = input("Choose an option: ")
				match users_choice_screen_saver:
					case "1":
						print("""
			=== Call Settings === """)
						in_call_settings = True
						while in_call_settings:
							print("""
			1. Automatic redial
			2. Speed dialling
			3. Call waiting
			4. Own number sending
			5. Phone line in use
			6. Automatic answer

				<-- 00. Back 
							""")
							users_choice_call_settings = input("Choose an option: ")
							match users_choice_call_settings:
								
								case "1":
									print("""
			=== Set Automatic Redial Here === """)
									in_automatic_redial = True
									while in_automatic_redial:
										print("""


				00 <-- Back
				 						""")
										users_choice_automatic_redial = input("Choose an option: ")
										match users_choice_automatic_redial:
											case "00":
												in_automatic_redial  = False
											case _:
												print("Invalid Input")
												continue
								case "2":
									print("""
			=== Set Speed Dial Here === """)
									in_speed_dialling_settings = True
									while in_speed_dialling_settings:
										print("""


				00 <-- Back
				 						""")
										users_choice_speed_dialling_settings = input("Choose an option: ")
										match users_choice_speed_dialling_settings:
											case "00":
												in_speed_dialling_settings  = False
											case _:
												print("Invalid Input")
												continue
								case "3":
									print("""
			=== Set Call Waiting Options Here === """)
									in_call_waiting = True
									while in_call_waiting:
										print("""


				00 <-- Back
				 						""")
										users_choice_call_waiting = input("Choose an option: ")
										match users_choice_call_waiting:
											case "00":
												in_call_waiting  = False
											case _:
												print("Invalid Input")
												continue
								case "4":
									print("""
			=== Own Number Sending Here === """)
									in_own_number = True
									while in_own_number:
										print("""


				00 <-- Back
				 						""")
										users_choice_own_number = input("Choose an option: ")
										match users_choice_own_number:
											case "00":
												in_own_number  = False
											case _:
												print("Invalid Input")
												continue
								case "5":
									print("""
			=== Set Phone Line in Use Here === """)
									in_phone_line_settings = True
									while in_phone_line_settings:
										print("""


				00 <-- Back
				 						""")
										users_choice_phone_line_settings = input("Choose an option: ")
										match users_choice_phone_line_settings:
											case "00":
												in_phone_line_settings   = False
											case _:
												print("Invalid Input")
												continue
								case "6":
									print("""
			=== Set Automatic answer Here === """)
									in_automatic_answer = True
									while in_automatic_answer:
										print("""


				00 <-- Back
				 						""")
										users_choice_automatic_answer = input("Choose an option: ")
										match users_choice_automatic_answer:
											case "00":
												in_automatic_answer  = False
											case _:
												print("Invalid Input")
												continue						
										
								case "00":
									in_call_settings = False
								case _:
									print("Invalid Input")
									continue
					
					case "2":
						print("""
			=== Phone Settings === """)
						in_phone_settings = True
						while in_phone_settings:
							print("""
			1. Language
			2. Cell info display
			3. Welcome note
			4. Network Selection
			5. Lights
			6. Confirm SIM service actions

				<-- 00. Back 
							""")
							users_choice_phone_settings = input("Choose an option: ")
							match users_choice_phone_settings:
								
								case "1":
									print("""
			=== Set Language Settings Here === """)
									in_language_settings = True
									while in_language_settings:
										print("""


				00 <-- Back
				 						""")
										users_choice_language_settings = input("Choose an option: ")
										match users_choice_language_settings:
											case "00":
												in_language_settings  = False
											case _:
												print("Invalid Input")
												continue
								case "2":
									print("""
			=== Set Cell Info Display Here === """)
									in_cell_display = True
									while in_cell_display:
										print("""


				00 <-- Back
				 						""")
										users_choice_cell_display = input("Choose an option: ")
										match users_choice_cell_display:
											case "00":
												in_cell_display  = False
											case _:
												print("Invalid Input")
												continue
								case "3":
									print("""
			=== Set Welcome Note Here === """)
									in_welcome_note = True
									while in_welcome_note:
										print("""


				00 <-- Back
				 						""")
										users_choice_welcome_note = input("Choose an option: ")
										match users_choice_welcome_note:
											case "00":
												in_welcome_note = False
											case _:
												print("Invalid Input")
												continue
								case "4":
									print("""
			=== Choose Networks Here === """)
									in_network_selection = True
									while in_network_selection:
										print("""


				00 <-- Back
				 						""")
										users_choice_network_selection = input("Choose an option: ")
										match users_choice_network_selection:
											case "00":
												in_network_selection  = False
											case _:
												print("Invalid Input")
												continue
								case "5":
									print("""
			=== Light Settings Here === """)
									in_light_settings = True
									while in_light_settings:
										print("""


				00 <-- Back
				 						""")
										users_choice_light_settings = input("Choose an option: ")
										match users_choice_light_settings:
											case "00":
												in_light_settings   = False
											case _:
												print("Invalid Input")
												continue
								case "6":
									print("""
			===Confirm SIM service actions Here === """)
									in_sim_service = True
									while in_sim_service:
										print("""


				00 <-- Back
				 						""")
										users_choice_sim_service = input("Choose an option: ")
										match users_choice_sim_service:
											case "00":
												in_sim_service = False
											case _:
												print("Invalid Input")
												continue						
										
								case "00":
									in_phone_settings = False
								case _:
									print("Invalid Input")
									continue
					#
					case "3":
						print("""
			=== Security Settings === """)
						in_security_settings = True
						while in_security_settings:
							print("""  
			1. PIN code request
			2. Call barring service
			3. Fixed dialling
			4. Closed user group
			5. Phone security
			6. Change access codes

				<-- 00. Back 
							""")
							users_choice_security_settings = input("Choose an option: ")
							match users_choice_security_settings:
								
								case "1":
									print("""
			=== PIN code request Here === """)
									in_pin_code_settings = True
									while in_pin_code_settings:
										print("""


				00 <-- Back
				 						""")
										users_choice_pin_code_settings = input("Choose an option: ")
										match users_choice_pin_code_settings:
											case "00":
												in_pin_code_settings  = False
											case _:
												print("Invalid Input")
												continue
								case "2":
									print("""
			=== Call barring service Here === """)
									in_call_barring = True
									while in_call_barring:
										print("""


				00 <-- Back
				 						""")
										users_choice_call_barring = input("Choose an option: ")
										match users_choice_call_barring:
											case "00":
												in_call_barring  = False
											case _:
												print("Invalid Input")
												continue
								case "3":
									print("""
			=== Set Fixed Dialling Here === """)
									in_fixed_dialling = True
									while in_fixed_dialling:
										print("""


				00 <-- Back
				 						""")
										users_choice_fixed_dialling = input("Choose an option: ")
										match users_choice_fixed_dialling:
											case "00":
												in_fixed_dialling = False
											case _:
												print("Invalid Input")
												continue
								case "4":
									print("""
			=== Set Closed User Group Here === """)
									in_closed_user_group = True
									while in_closed_user_group:
										print("""


				00 <-- Back
				 						""")
										users_choice_closed_user_group = input("Choose an option: ")
										match users_choice_closed_user_group:
											case "00":
												in_closed_user_group  = False
											case _:
												print("Invalid Input")
												continue
								case "5":
									print("""
			=== Set Phone Security Here === """)
									in_phone_security = True
									while in_phone_security:
										print("""


				00 <-- Back
				 						""")
										users_choice_phone_security = input("Choose an option: ")
										match users_choice_phone_security:
											case "00":
												in_phone_security   = False
											case _:
												print("Invalid Input")
												continue
								case "6":
									print("""
			=== Change Access Codes Here === """)
									in_access_codes = True
									while in_access_codes:
										print("""


				00 <-- Back
				 						""")
										users_choice_access_codes = input("Choose an option: ")
										match users_choice_access_codes:
											case "00":
												in_access_codes = False
											case _:
												print("Invalid Input")
												continue						
										
								case "00":
									in_security_settings = False
								case _:
									print("Invalid Input")
									continue
					#
					case "4":
						print("""
			=== Reset Device To Factory Default === """)
						in_reset_default = True
						while in_reset_default:
							print("""
			If you reset to factory default all
			data might be lost.

			01. Continue			00 <-- Back
				 			""")
							users_choice_reset_default = input("Choose an option: ")
							match users_choice_reset_default:
								case "01":
									print("""
			=== Factory reset complete === """)
									in_reset_complete = True
									while in_reset_complete:
										print("""
			Factory reset has been complete and all
			data not backed up has been lost.

				<-- 00. Back to Main Menu 
										""")
										users_choice_reset_complete = input("Choose an option: ")
										match users_choice_reset_complete:
											case "00":
												in_reset_complete = False
												in_reset_default = False
												in_settings = False
											case _:
												print("Invalid Input")
												continue
									
								case "00":
									in_reset_default = False
								case _:
									print("Invalid Input")
									continue
						
					case "00":
						in_settings = False
					case _:
						print("Invalid Input")
						continue
		case "7":
			print("""
			=== Set Call Divert Here === """)
			in_call_divert = True
			while in_call_divert:
				print("""



				00 <-- Back
				 """)
				users_choice_call_divert = input("Choose an option: ")
				match users_choice_call_divert:
					case "00":
						in_call_divert = False
					case _:
						print("Invalid Input")
						continue
		case "8":
			print("""
			=== Choose Game Here === """)
			in_games = True
			while in_games:
				print("""
			1. Rock Paper Scissor(Free Trial)		


				00 <-- Back
				 """)
				users_choice_in_games = input("Choose an option: ")
				match users_choice_in_games:
					case "1": 
						in_rock_paper = True
						while in_rock_paper:
							play_rock_paper_scissor()
							print("""
			==== Rock Paper Scissor ===
			Do you want to continue

			1.Yes		<-- 00. Main """)
							users_choice_rock_paper = input("Choose an option: ")
							match users_choice_rock_paper:
								case "1": 
									continue
								case "00":
									in_rock_paper = False
									in_games = False
								case _:
									print("Invalid input")


					case "00":
						in_games = False
					case _:
						print("Invalid Input")
						continue
		case "9":
			print("""
			=== Calculator === """)
			in_calculator = True
			while in_calculator:
				print("""



				00 <-- Back
				 """)
				users_choice_calculator = input("Choose an option: ")
				match users_choice_calculator:
					case "00":
						in_calculator = False
					case _:
						print("Invalid Input")
						continue
		case "10":
			print("""
			=== Set Reminders Here === """)
			in_reminder = True
			while in_reminder:
				print("""



				00 <-- Back
				 """)
				users_choice_reminder = input("Choose an option: ")
				match users_choice_reminder:
					case "00":
						in_reminder = False
					case _:
						print("Invalid Input")
						continue
		case "11":
			print("""
			=== Clock === """)
			in_clock = True
			while in_clock:
				print("""
			1. Alarm Clock
			2. Clock Settings
			3. Date setting
			4. Stopwatch
			5. Countdown timer
			6. Auto update of data and time

				<-- 00. Back """)
				users_choice_clock = input("Choose an option: ")
				match users_choice_clock:
					case "1":
						print("""
			=== Set Alarm Clock Here === """)
						in_alarm = True
						while in_alarm:
							print("""



				00 <-- Back """)
							users_choice_alarm = input("Choose an option: ")
							match users_choice_alarm:
								case "00":
									in_alarm = False
								case _:
									print("Invalid Input")
									continue
					case "2":
						print("""
			=== Set Clock Here === """)
						in_clock_settings = True
						while in_clock_settings:
							print("""



				00 <-- Back """)
							users_choice_clock_settings = input("Choose an option: ")
							match users_choice_clock_settings:
								case "00":
									in_clock_settings = False
								case _:
									print("Invalid Input")
									continue
					case "3":
						print("""
			=== Set Date Here === """)
						in_date_settings = True
						while in_date_settings:
							print("""



				00 <-- Back """)
							users_choice_date_settings = input("Choose an option: ")
							match users_choice_date_settings:
								case "00":
									in_date_settings = False
								case _:
									print("Invalid Input")
									continue
					case "4":
						print("""
			=== Set Stopwatch Here === """)
						in_stopwatch = True
						while in_stopwatch:
							print("""
			
			
				00 <-- Back """)
							users_choice_stopwatch = input("Choose an option: ")
							match users_choice_stopwatch:
								case "00":
									in_stopwatch = False
								case _:
									print("Invalid Input")
									continue
					case "5":
						print("""
			=== Set Countdown Here === """)
						in_countdown = True
						while in_countdown:
							print("""
			
			
				00 <-- Back """)
							users_choice_countdown = input("Choose an option: ")
							match users_choice_countdown:
								case "00":
									in_countdown = False
								case _:
									print("Invalid Input")
									continue
					case "6":
						print("""
			=== Auto Update Date and Time === """)
						in_udpate_date_and_time = True
						while in_udpate_date_and_time:
							print("""
			
			
				00 <-- Back """)
							users_choice_udpate_date_and_time = input("Choose an option: ")
							match users_choice_udpate_date_and_time:
								case "00":
									in_udpate_date_and_time = False
								case _:
									print("Invalid Input")
									continue
						
					case "00":
						in_clock = False
					case _:
						print("Invalid Input")
						continue
		case "12":
			print("""
			=== Set Profiles Here === """)
			in_profiles = True
			while in_profiles:
				print("""



				00 <-- Back
				 """)
				users_choice_profiles = input("Choose an option: ")
				match users_choice_profiles:
					case "00":
						in_profiles = False
					case _:
						print("Invalid Input")
						continue
		case "13":
			print("""
			=== Choose SIM services Here === """)
			in_sim_services = True
			while in_sim_services:
				print("""



				00 <-- Back
				 """)
				users_choice_sim_services = input("Choose an option: ")
				match users_choice_sim_services:
					case "00":
						in_sim_services = False
					case _:
						print("Invalid Input")
						continue
							
		case "00": 
			running = False 
		case _:
			print("Invalid Input")
			continue	



















