def calculate_word_match(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    
    common_words = words1.intersection(words2)
    
    total_words = len(words1.union(words2))
    match_percentage = (len(common_words) / total_words) * 100 if total_words > 0 else 0
    
    return common_words, match_percentage

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

common_words, match_percentage = calculate_word_match(text1, text2)

print(f"Sakritīgie vārdi: {', '.join(common_words)}")
print(f"Sakritības līmenis: {match_percentage:.2f}%")
