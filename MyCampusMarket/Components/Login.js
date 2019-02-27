import React from 'react'
import { StyleSheet, View, TextInput, Button, Text } from 'react-native'

class Login extends React.Component {
  render() {
    return (
      <View style={styles.main_container}>
        <View style={styles.intro}>
          <Text style={styles.baseText}>Connecte-toi :</Text>
          <TextInput style={styles.textInput} placeholder= "Surnom/Email"/>
          <TextInput secureTextEntry={true} style={styles.textInput} placeholder= "Mot de passe"/>
        </View>
        <View style={styles.buttons}>
          <Button title="Se connecter" onPress={() => {this.props.navigation.navigate("GlobalMarketView")}} style={styles.buttons}/>
          <Text style={styles.titleText}>OU</Text>
          <Button title='Se connecter avec Facebook' onPress={() => {}} style={styles.facebookButton}/>
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
    flex: 1,
    marginTop: 20,
    fontSize: 20,
    fontWeight: 'bold',
  },
  textInput:{
    borderColor: '#000000',
    borderWidth: 1,
    backgroundColor: '#ffffff',
    marginLeft: 100,
    marginRight: 100,
    flex: 0,
    marginTop: 5,
    fontFamily: 'sans-serif',
    textAlign: 'center'
  },
  buttons: {
    flex: 1,
    marginTop: 0,
    borderRadius: 20,
    marginLeft:20,
    marginRight:20,
    alignItems: 'center',

  },
  facebookButton: {
    flex: 1,
  },
  cgu: {
    flex: 3,
    textDecorationLine: 'underline',
  },
})

export default Login
