* `root` - touchdesigner project used for compositing together the final image
* `modules/comfyui` - all of the comfyui related stuff. workflows and reference images

there’s basically 3 parts that need to be addressed.
1) The overlaying of blood onto the subject
2) the compositing of the killers arm in the background
3) the compositing of the look/mood and brand styling

(1) is the one I’ve continued to have trouble with cause I’m just struggling to make it look any good. Latest attempt is a method of getting a normal map generated from the image and using displacement to warp a decal onto the subject. 
There's also a version in the TD project where a quad is being deformed by the normal map and composited back onto the original image. Both versions work about as well as the other so I think it's more about visual preference and workflow at that point.

(2) I think is pretty straight forward and I already have a segmented image of the subjects that can be used to put them in front of the killers arm. *NOTE: The segmented image is in the workflow, compositing still needs to be finished.*

(3) is just overlay graphics and color tweaking so that just needs to be composited. *NOTE: Still needs to be implemented*

