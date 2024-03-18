## ncatweb
ncatweb is a visualization of the pages on [https://ncatlab.org/](https://ncatlab.org/) (specifically the pages here [https://ncatlab.org/nlab/all_pages](https://ncatlab.org/nlab/all_pages)) as of March 8th, 2024. This achieved by parsing the links on each page and creating JSON files that can be utilized by the [3d-force-grap](https://github.com/vasturiano/3d-force-graph).

### Data files
The data files are split up into each page linking to 3, 10, 5, 50, and all other pages. 
| file        | nodes       | edges     |
| ----------- | ----------- | --------- |
| data3.json  | 27418       | <82254    |
| data5.json  | 27418       | <137090   |
| data10.json | 27418       | <274180   |
| data50.json | 27418       | <1370900  |
| dataAll.json| 27418       | <Infinity | (good luck running)

I have also included `pages.zip` which consists of all the raw html data of every page on nlab which was used to generate the graph data.

### Visualization
To change which file you are visualizing change the file linked in `index.html`. Bigger data files with take much longer to render. To visualize, start a python web server with `python -m http.server`. Then navigate to your local host in a web browser. 

### Issues
Google Chrome has a limit of memory and thus doesn't work for loading some of the bigger files. This has only been tested and shown to work in Firefox.

