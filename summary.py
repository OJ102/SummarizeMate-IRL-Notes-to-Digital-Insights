import cohere 
co = cohere.Client('MB5Tg4Xti81PqzLjKC24GqCn2IAocX3NRLLVi7TE') # This is your trial API key
response = co.summarize( 
  text='\n\n	Please use the sharing tools found via the share button at the top or side of articles. Copying articles to share with others is a breach of FT.com T&Cs and Copyright Policy. Email licensing@ft.com to buy additional rights. Subscribers may share up to 10 or 20 articles per month using the gift article service. More information can be found at https://www.ft.com/tour.\n	https://www.ft.com/content/d301c852-6160-4be2-80b0-46b26c7066e5\n\n	Antony Blinken faced intense pressure from close regional allies to facilitate an immediate ceasefire in Gaza, laying bare the stark gap between US support for Israel and the outrage in Arab capitals over the siege and bombardment of the strip.\n\n“We need to work together . . . to stop this madness,” Jordan’s foreign minister, Ayman Safadi, told the US secretary of state after a day of meetings with Arab diplomats.\n\nSameh Shoukry, the Egyptian foreign minister, demanded an immediate, unconditional ceasefire, a commitment that Benjamin Netanyahu bluntly rejected after meeting Blinken on Friday. The US had urged the Israeli prime minister to allow for “humanitarian pauses”.\n\nThe meeting in the Jordanian capital Amman took place as fierce battles raged in Gaza, including an incursion by the Israeli military into the south of the enclave, where it has repeatedly told civilians to flee.\n\nIsrael’s forces allowed a three-hour window earlier on Saturday for the estimated 300,000 Palestinians still in northern Gaza to travel south.\n\nAbout 9,500 Palestinians have been killed in Gaza since October 7, when Israel began its aerial bombardment, followed by a ground invasion a week ago, local health officials said.\n\nAt least 1,400 Israelis were killed in Hamas’s cross-border raid, Israeli authorities said. Twenty-seven soldiers have been killed by Hamas militants inside Gaza.\n\nThe fighting intensified on Friday after Netanyahu rejected Blinken’s call for a “humanitarian pause”, saying any ceasefire would require the immediate release of all 242 hostages held by Hamas. Blinken said he had urged Israel to “do more to protect Palestinian civilians.”\n\n“We believe pauses can be a critical mechanism for protecting civilians, for getting aid in, for getting foreign nationals out while still enabling Israel . . . to defeat Hamas,” Blinken said in Amman earlier on Saturday.\n\nIn the hours after Blinken’s visit to Tel Aviv, Israeli air strikes struck at least one ambulance heading to the Dar al-Shifa hospital in Gaza City, and then another explosion hit the rest of the convoy near the entrance to the building. Video from the scenes showed civilian casualties, including women and children.\n\nThe Israeli military said the convoy it had struck was “being used by a Hamas operative”, and claimed that several Hamas militants were killed.\n\nBlinken had been expected to “brainstorm” with Arab diplomats the future of Gaza, home to 2.3mn Palestinians, after the war with Hamas ends. Safadi bluntly rejected those talks as premature.\n\n“How can we even entertain what will happen in Gaza when we do not know how Gaza will be left?” he told Blinken. “Are we going to be talking about a wasteland? Are we talking about a whole population reduced to refugees?”\n\nThe publicly expressed frustration matched the tone of the day-long meetings, an Arab official briefed on the talks said. Arab leaders want progress towards a ceasefire and more humanitarian aid before a summit in Riyadh next week, they said.\n\nJordan has already withdrawn its ambassador to Israel, and Egypt is concerned that Israel is attempting to use the war in Gaza to displace Palestinians into the neighbouring Sinai peninsula.\n\nInternational efforts to get more aid into the enclave while simultaneously creating conditions for the release of Hamas’s hostages, many of them women, children and the elderly, continued but there was no breakthrough in sight, diplomats said.\n\nA senior US administration official said on Friday that intense discussions to secure the release of 242 hostages in Gaza were still taking place, including through indirect engagement with Hamas.\n\nThe official added that the October 20 release of two American hostages — a mother and her teenage daughter — was a test run to see if the channel for hostage discussions, which includes Qatar and Egypt, was feasible and whether the parties could secure a pause in the fighting to facilitate their release.\n\nHamas has demanded a ceasefire, more aid for Palestinian civilians and fuel for the strip, in exchange for the release of civilians, while it intends to hold on to captured Israeli soldiers to trade for more than 6,000 Palestinians held in Israeli prisons.\n\nAid convoys from Egypt into Gaza remained at a fraction of prewar levels, with Israeli security examining the contents of each truck before it is allowed into the enclave.\n\nSince hostilities began on October 7, 410 trucks have entered the strip, 36 of them on Friday, according to an Israeli ministry of defence document seen by the Financial Times. More than 400 trucks a day entered the enclave before the fighting began.\n\nIsrael blamed the delays on “logistical difficulties among the organisations responsible for receiving the humanitarian aid”, and maintained that there was enough food and water in the “short term”.\n\nInternational organisations, including the UN, have documented a widespread humanitarian crisis, and Tom White, the Gaza director for the UN agency for Palestinian refugees, UNRWA, said on Friday that the average Gazan was now living on two pieces of bread a day, and begging for clean water.\n',
  length='auto',
  format='auto',
  model='command',
  additional_command='',
  temperature=0.3,
) 
print('Summary:', response.summary)