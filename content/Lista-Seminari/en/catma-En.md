---
id-asset: "02"
title: "catma"
description: Seminario fake su lessico e ripetizione.
videoLink: 
- "https://www.youtube.com/watch?v=OHgy75FqOZk"  
videoThumbnail: "https://www.wpbeginner.com/wp-content/uploads/2013/07/get-the-post-thumbnail-url-in-wordpress-og.png"  
videoLabel: "Watch video"
tags:
- "#ob/tre"
- "#ob/uno"
- "#ob/animali"
layout: ["seminar", "altro"]
seminar-date: "21.06.2024"
seminar-title: "..."
seminar-description: "..."
seminar-author-codekey: 
- codauthor1
- codauthor2
seminar-author-affiliation: "..."
seminar-author-affiliation-unibo: ["no", "yes"]
seminar-video-title: "..."
seminar-video-link: "video-link"
seminar-video-thumbnail-link: "video-link"
seminar-video-length: 2h
tutorial-agent-type: ["human", "machine"]
tutorial-extended-title: "..."
tutorial-short-title: "catma"
tutorial-author-codkey: "codkey"
tutorial-video-agent-type: ["human", "machine"]
tutorial-video-extended-title: "..."
tutorial-video-short-title: "..."
tutorial-video-author-codkey: "codkey"
translation: ["language", "link"]
status: ["draft", "finished"]
resources:  
- type: video  
  title: Interview video  
  url: https://example.com/video  
  thumbnail: /img/thumb1.jpg  
- type: pdf  
  title: Slides  
  url: /docs/slides.pdf  
- type: image  
  title: Poster  
  url: /img/poster.jpg
---


%%layout: seminar
title: "Annotazione e Analisi di Testi Digitali con CATMA 7"
title-short: "catma"
seminar_title: "Digital Text Annotation and Analysis with CATMA 7"
date: "21.06.2024"
author-tutorial: esmeraldadivenere
author-seminar: mariakazawa
video-title: "Digital Text Annotation and Analysis with CATMA 7"
video-link-seminar: "https://liveunibo-my.sharepoint.com/personal/ludovica_pannitto_unibo_it/_layouts/15/stream.aspx?id=%2Fpersonal%2Fludovica%5Fpannitto%5Funibo%5Fit%2FDocuments%2FSEMINARI%20LAB%2FVideo%2FDigital%20Text%20Annotation%20and%20Analysis%20with%20CATMA%207%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E29d9f385%2D5185%2D490a%2D8cc3%2Dba9f215993da"
video-length: 2h
affiliation-unibo: yes
translation:
  - ["en", "/seminari/en/catma.html"]
%%

# Catma
Catma stands for **Computer Assisted Text Markup and Analysis**. Offered since 2018, it is a free open source text annotation tool particularly suitable for manual text annotation. It is used to do both qualitative and quantitative anaylisis on linguistic and literary features of texts.
Catma also supports collaborative work not only in the annotation process, but also in managing data, project members and results.


_________________

# Account and Login
Go to the website https://catma.de/ and click on "Work with CATMA". You can create an account using a private e-mail or a Google account.

[#TODO sostituire immagine con figure]
<img src="Catma-Sign.PNG" width="916.8" height="412">

After signing up, you will receive a verification e-mail to the address used for registration. Once your e-mail address has been verified, you will be able to complete your profile by choosing username and pasword.
Once you have set your username and password, you are ready to initiate your first project.

_________________

# Project Module
After you have logged into your account, you will be taken to the project overview.
You will receive an overview of existing projects which are coloured in grey and you will see that you have the option to either **join** a project or to **create** a new project.

[#TODO sostituire immagine con figure]
<img src="Catma-Home.PNG" width="882" height="416.4">

There is also a sidebar which is still deactivated but which will be activated as soon as you have entered your project and it guides you through the different modules.
On entering the project module by selecting a project, you will be able to manage its components and each component class is displayed in a tile.

[#TODO sostituire immagine con figure]
<img src="Catma-Project.PNG" width="903.6" height="418.8">

There is a tile for Documents & Annotations, one for the Tagsets belonging to this project and one for the Project Members.

In the tile for **Documents & Annotations**, you can see and upload projects.
You can upload those texts from your local computer or you can add an URL.Then you will get a preview of how the document will be displayed, you can adapt for example the character and the language of the text. In the next set you will be able to add information like author, publisher or description. You then choose a pattern for the generation of the annotation collections. Once you click on "Finish" the document will be displayed in the Documents & Annotations tyle. If you want to add another annotation collection for this document, you click on the document and then the plus icon, select "annotation collection", enter a name. You will see now that the annotation collection is displayed beneath the associated document.
You can also delete the tags and annotation collections and export collections or documents, including your annotations.
In order to annotate the documents, you will always first have to create an annotation collection.

You will also see which person has created a resource and who is therefore responsible for it. Please note that you can only add an annotation collection if your project role allows it, because in Catma there are different *roles* tied to different permissions. [spostare a Members] We have *partners*, *assistants* and *owners*.
Owners create the project and have all the rights you can think of. A partner can do everything except manage members or delete a project. Assistants don't have any project administration rights and cannot create or delete resources, but they can view resources and tags as texts or annotations.

Then in the second tile you can see the **Tagsets** (a sort of container of tags). Here you can also create a new tag, delete tags or add to them. Notice though that you can create new tagsets, but if you want to actually add a tag to a tagset, you will have to do this in the [Tags module](#tags-module). To edit a tag, you can do it by double-clicking on it or by entering the Tags Module.

The third tile in the project module, we see the Project **Members**, it will display at least the project owner as well as the role of the project owner or the project member.
If your role allows it, you can add Members of this project by either joining manually (by clicking the plus icon and adding his or her username), or via invitation in real time (by clicking on the three dots). If you choose the latter, the invitation in a real time pop up dialogue with a code will appear, and everyone who has access to the code will be able to join the project. This code will be valid as long as you keep the pop up window opened and then it won't be valid anymore.
You can see the synchronise SYNC button in the upper right corner and whenever you work together with others in a collaborative project, each individual team member has to synchronise his or her project progress in order to share their uploaded documents, annotations or new tags with the other team members. So clicking this button starts the process of integrating your changes with the most recent integrated project stage. In other words, it attempts to integrate anything you have done since you last synchronised.

Switch Button or the Switch view button on the left of the synchronise button is enabled to allow for switching between two view modes: synchronised and latest contributions. The first shows the current state of all work that has been integrated, plus anything that you as an individual user have done on top of that, the second allows for read only access to all project members’ latest works.

_________________

# Tags Module
If you want to create a tag set you have to switch into the tags module. The tags module displays the tagsets of your projects. You can see which of these tagsets are currently selected as well as the exit (?) ones, by extending the grey ledge on the left. To add a new tag to a tagset, select the tagset, click on the plus icon, then "Add Tag" and choose a name (if you want, you can add properties).
You can create **subtags** and **properties** for your tags. A subtag is a tag that is sub ordinated to another tag in the tag hierarchy and properties are means to further qualify an annotation (you can add properties to a sub tag as well as normal tags).

[#TODO sostituire immagine con figure]
<img src="Catma-Tags.PNG" width="914.4" height="419.4">

_________________

# Annotate Module
Once your project contains at least one document, one annotation collection and a text set, you can start to annotate a document in CATMA's annotate module.
When you click on the A. Module, the grey ledge will automatically unfold in order to make you choose your annotation collection and the tagset.
Now you can see the text on the left side and the tagset. If the tagset is still disabled, you can enable it by clicking on the eye icon.

To start annotating, you select a text passage, then do a right click or use the pane on the right, choose the tagset and the property.

It is also possible to annotate discontinuous passages in order to do so, you have to click on the book icon and you can now select many passages from the text and then apply one tag.

You can tag the same text passage multiple times.

There's also the opportunity to leave comments, by selecting a text passage and clicking on the specific icon.

_________________

# Analyze module
In the analyse module you can explore texts and annotations with queries and visualisations. You will have the query builder on the left side and the visualisation options on the right side.
Queries allow you to analyse, explore and evaluate text or annotation data. To execute a query on documents or annotation collections you have three options:

- Select a predefined query
- Use the query builder to create your own query
- Type in a query directly (if you're familiar with cATMAì's query language)

Once your query has been executed, you can explore your results displayed in a box beneath the query fields wth a headline with the query itself, a timestamp, and the total number of results.

Another option to explore your query's results is by using the Visualisations.
