import sys
import json
import torch
import numpy as np
import pandas as pd    

from transformers import ( BertForSequenceClassification, BertTokenizer)

class applyNLP():

  device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

  model = BertForSequenceClassification.from_pretrained("neuralmind/bert-base-portuguese-cased")

  model.load_state_dict(torch.load('/opt/nifi/nifi-current/scripts/pytorch_model.bin',map_location=torch.device('cpu')))

  tokenizer = BertTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')


  def encoded_review(self, text) -> object:
    return self.tokenizer.encode_plus(
            text,
            max_length=512,
            add_special_tokens=True,
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt',
          )


  def predict(self, review_text) -> list:
    preds = []
    for text in review_text:

      input_ids = self.encoded_review(text)['input_ids'].to(self.device)

      attention_mask = self.encoded_review(text)['attention_mask'].to(self.device)

      output = self.model(input_ids, attention_mask)

      _, prediction = torch.max(output.logits, dim=1)

      preds.append(prediction.cpu().numpy())

    return np.concatenate(preds)


  def main(self, input):
    df = pd.DataFrame(input)

    predicted = self.predict(df.text.values)

    df["sentiment"] = predicted

    return df.to_json(orient='records', force_ascii = False)



if __name__ == "__main__":

  inn = json.loads(sys.stdin.read())

  print(applyNLP().main(inn))