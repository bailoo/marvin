# marvin
ML-based approach to Artist Recommendation by StarClinch

## [StarClinch.com](https://starclinch.com)
StarClinch is the Indias largest online platform for booking performance artists and entertainers including Singers, Comedians, Celebrities,  Live Bands, DJs, Anchors, and Speakers for all type of Events ranging from Campus Events to Wedding Ceremonies. 
StarClinch gets approximately 100 queries daily from clients for 18,000+ registered Artists.

`Clients` have two options to book Artists for their Events. First, Client can search for artists using the [online platform](https://starclinch.com) and get Quotes for that Artist directly. Second, Clients can fill the Post Your Requirements [PYR](https://starclinch.com/requirement.html) form and submit it then, one of the Business team members would contact the Client to get more information regarding the event based on that Business Team would then pitch artists to the client which fall into the required category and budget. The second options require manual work from gathering information about the event to pitching artists to the client. 

`Marvin` project aims to automate the process of pitching artists to the users based on the information in the PYR Form.

---

### Data

Post Your Requirements and Get Your Quote both requires some basic information need to be filled out.

`Artists Category`: Type of Artists required for the Event for example Singer, DJ or Celebrity.<br>
`Event`: Type of Event for example Campus, Wedding, Private Party or Corporate.<br>
`Budget`: A rough approximate of Budget for the Event.<br>
`Gathering`: Gathering Size that is Number of People that are going to attending the event.<br>
`Location or Venue`: Location (Address or Venue) of the Event.<br>
`Date`: Event Date.<br>
`Client Details`: Name, Phone Number and Email Address of the Client.<br>

The difference between PYR & GTQ is that GTQ would also have the name of the artist that the client wants to book for his/her event whereas the PYR won't. Whether it's a GTQ request or a PYR request both are considered as a Deal and are stored in StarClinch Pipedrive each Deal have a unique ID associated with it along with all the necessary information. 

`DealDetails.py` contains python class `Deals` to fetch the Deals data using Pipedrive API, parse the data (from JSON Format to Human readable Format) and store it in a CSV File.

---

### Installation

To run the Jupyter Notebook and Python Scripts we need few libraries.

```shell
git clone https://github.com/bailoo/marvin.git
cd marvin
pip (or pip3) install -r requirements.txt
```
