# HP_Cartridge_Identifier
Cartridge type identifier, based on computational vision, for a hackathon of HP (october 2023). We used opencv to extract useful information from the cartridge images, specially label content and color to separate the black type from the colored type.

## Dependencies:
  - open cv >= 4.8.0

## How does it works?
The system is basically a classifier; we feed the images of th cartridges, with their labels pointing to the camera, and the open cv will extract the information from the label and the colour of the cover. The output is the category of that cartridge, per type (664, 667 or 57) or per color (colored or black).

## How to use it?
It's simple

Import the classifier:
```
import src.cartridge_classifier as cartridge_classifier
```

Load the image:

```
img = cartridge_classifier.CartridgeImage(<img_path>)
```

Test the classifier:

```
cart_class = img.extract_cartridge_type()
>>>664
```
