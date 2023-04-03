import joblib
import sys 
from PIL import Image

img_path = sys.argv[1]
#print(img_path)

img =  Image.open(img_path).convert("RGB")

#print('Image shape', img.size)



model_loaded = joblib.load('../../models/generation/model.pkl')
tokenizer_loaded = joblib.load('../../models/generation/tokenizer.pkl')
feature_extractor_loaded = joblib.load('../../models/generation/feature_extractor.pkl')

generated_caption = tokenizer_loaded.decode(model_loaded.generate(feature_extractor_loaded(img, return_tensors="pt").pixel_values.to("cuda"))[0], 
                                            skip_special_tokens=True)

print(generated_caption)

os.makedirs("results", exist_ok=True)

save_name = img_path.rsplit(os.path.sep, 3)[1:]
save_name = '/'.join(save_name)
save_name = save_name.replace(save_name.rsplit('.', 1)[-1], 'json')
save_name = save_name.replace(os.path.sep, '_')
#print(save_name)
save_path = '/'.join(["results", save_name])
print(save_path)
with open(save_path, 'w') as temp:
    temp.write(generated_caption)

