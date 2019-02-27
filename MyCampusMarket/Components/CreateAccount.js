import React from 'react'
import { StyleSheet, View, TextInput, Button, Text } from 'react-native'

class CreateAccount extends React.Component {
  render() {
    return (
      <View style={styles.main_container}>
        <View style={styles.intro}>
          <Text style={styles.baseText}>Remplis les champs ci-dessous :</Text>
          <TextInput style={styles.textInput} placeholder= "Prénom"></TextInput>
          <TextInput style={styles.textInput} placeholder= "Nom"></TextInput>
          <TextInput style={styles.textInput} placeholder= "Surnom"></TextInput>
          <TextInput style={styles.textInput} placeholder= "Email"></TextInput>
          <TextInput secureTextEntry={true} style={styles.textInput} placeholder= "Mot de passe"></TextInput>
          <TextInput secureTextEntry={true} style={styles.textInput} placeholder= "Confirmation mot de passe"></TextInput>
        </View>
        <View style={styles.boutons}>
          <Button title="C'est parti !" onPress={() => {this.props.navigation.navigate("Tutorial")}} style={styles.buttons}/>
          <Button title='Utiliser mon compte Facebook' onPress={() => {}} style={styles.facebookButton}/>
        </View>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  main_container: {
    flex: 1,
    marginTop: 20,
    backgroundColor: 'steelblue'
  },
  intro: {
    flex: 1,
    marginTop: 10,
  },
  baseText: {
    flex: 0,
    marginTop: 5,
    fontFamily: 'sans-serif',
    textAlign: 'center',
  },
  titleText: {
    flex: 2,
    marginTop: 20,
    fontSize: 20,
    fontWeight: 'bold',
  },
  textInput:{
    borderColor: '#000000',
    borderWidth: 1,
    backgroundColor: '#ffffff',
    marginLeft: 80,
    marginRight: 80,
    flex: 0,
    marginTop: 5,
    fontFamily: 'sans-serif',
    textAlign: 'center'
  },
  buttons: {
    flex: 2,
    marginTop: 0,
    borderRadius: 20,
    marginLeft:20,
    marginRight:20,
    alignItems: 'center',
  },
  facebookButton: {
    flex: 2,
    marginTop:0
  },
  cgu: {
    flex: 3,
    textDecorationLine: 'underline',
  },
})

export default CreateAccount
