import React from 'react'
import { StyleSheet, View, TextInput, Button, Text, Image, TouchableOpacity, TouchableHighlight } from 'react-native'

class Needs extends React.Component {
  render() {
    return (
    <View style={styles.main_container}>
      <Button 
        title={"Mes options"}
        style={styles.main_container}
        onPress={() => this.props.navigation.openDrawer()}/>   
        <View style={styles.intro}>
          <Text style={styles.baseText}>
            Les demandes
          </Text>
        </View>
        
      </View>
    )
  }
}

const styles = StyleSheet.create({
  main_container: {
    flex: 1,
    marginTop: 0,
    backgroundColor: 'steelblue'
  },
  icon: {
    width: 30,
    height: 30
  },
  intro: {
    flex: 1,
    marginTop: 50
  },
  baseText: {
    flex: 1,
    marginTop: 20,
    fontFamily: 'sans-serif',
    textAlign: 'center',
  },
  titleText: {
    flex: 2,
    marginTop: 20,
    fontSize: 20,
    fontWeight: 'bold',
  },
  buttons: {
    flex: 2,
    marginTop: 0,
    borderRadius: 20,
    marginLeft:20,
    marginRight:20,
    alignItems: 'center',
  },
  cgu: {
    flex: 3,
    textDecorationLine: 'underline',
  },
})

export default Needs
