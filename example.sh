#!/usr/bin/env bash

mkdir alice bob && \
cd alice && python3 ../crypto create public alice && cd .. && \
cd bob && python3 ../crypto create public bob && cd .. && \
mv alice/alice_public_key.dat bob && mv bob/bob_public_key.dat alice && \
echo "attack at dawn" > alice/plaintext.txt && \
echo "Alice's message is:" && cat alice/plaintext.txt && \
python3 crypto -p alice/alice_private_key.dat -P alice/bob_public_key.dat create seal alice/plaintext.txt && \
mv alice/seal_plaintext.dat bob && \
python3 crypto -p bob/bob_private_key.dat -P bob/alice_public_key.dat read seal bob/seal_plaintext.dat && \
echo "Bob reads Alice's message:" && cat bob/decrypted_plaintext.txt